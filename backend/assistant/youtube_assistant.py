from langchain_core.messages import HumanMessage

from backend.youtube.url import get_video_id
from backend.vectorstore.embeddings import get_embed
from backend.vectorstore.faiss_store import get_vectorstore
from backend.vectorstore.retriever import create_retriever
from backend.llm.model import create_llm
from backend.graph.graph import build_graph
from backend.database.postgres import Database

class YouTubeAssistant:
    def __init__(self):
        print("Creating YouTube Assistant...")

        self.embeddings = None
        self.model = None
        self.graph = None
        self.retriever = None
        self.video_id = None
        self.video_url = None
        self.database = Database()

        print("YouTube Assistant created.")

    def initialize_models(self):
        if self.embeddings is None:
            self.embeddings = get_embed()

        if self.model is None:
            self.model = create_llm()

    def load_video(self, url: str):

        if not url.strip():
            raise ValueError("YouTube URL cannot be empty.")

        video_id = get_video_id(url)
        print(f"Preparing video: {video_id}")

        # Models
        self.initialize_models()

        # Database
        checkpointer = self.database.initialize()

        # Vector store
        vectorstore = get_vectorstore(url,self.embeddings)

        # Retriever
        self.retriever = create_retriever(vectorstore)

        # Graph
        self.graph = build_graph(
            self.retriever,
            self.model,
            checkpointer
        )

        self.video_id = video_id
        self.video_url = url

        print(f"Video ready: {video_id}")
        return video_id

    def ask(
        self,
        question: str,
        thread_id: str
    ):

        if not question.strip():
            raise ValueError("Question cannot be empty.")

        if self.graph is None:
            raise ValueError("Please load a YouTube video first.")

        if not self.database.checkpointer:
            raise ValueError("PostgreSQL checkpointer is not initialized.")

        config = {
            "configurable": {"thread_id": thread_id}
        }

        response = self.graph.invoke(
            {
                "question": question,
                "messages": [HumanMessage(content=question)]
            },
            config=config )
        return response["answer"]

    def ask_stream(
        self,
        question: str,
        thread_id: str
    ):

        if not question.strip():
            raise ValueError( "Question cannot be empty.")

        if self.graph is None:
            raise ValueError("Please load a YouTube video first.")

        if not self.database.checkpointer:
            raise ValueError("PostgreSQL checkpointer is not initialized.")

        config = {
            "configurable": {"thread_id": thread_id}
        }

        for chunk in self.graph.stream(
            {
                "question": question,
                "messages": [HumanMessage(content=question)]
            },
            config=config,
            stream_mode="updates",
            version="v2"
        ):

            if chunk["type"] != "updates":
                continue

            updates = chunk["data"]

            if "generate" not in updates:
                continue

            generate_update = updates["generate"]
            answer = generate_update.get("answer")

            if not answer:
                continue

            words = answer.split(" ")
            for index, word in enumerate(words):
                if index == 0:
                    yield word
                else:
                    yield " " + word

    def close(self):
        self.database.close()
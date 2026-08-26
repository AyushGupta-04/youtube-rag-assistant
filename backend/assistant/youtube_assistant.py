from backend.youtube.url import get_video_id
from backend.vectorstore.embeddings import  get_embed
from backend.vectorstore.faiss_store import get_vectorstore
from backend.vectorstore.retriever import create_retriever
from backend.llm.model import create_llm
from backend.graph.graph import build_graph
from backend.database.postgres import Database
from langchain_core.messages import HumanMessage

class YouTubeAssistant:
    def __init__(self):
        print("Creating YouTube Assistant...")

        self.embeddings = None
        self.model = None
        self.database = Database()
        self.checkpointer = None
        self.graph = None
        self.retriever = None
        self.video_id = None
        self.video_url = None

        print("YouTube Assistant created.")

    # MODELS
    def initialize_models(self):
        if self.embeddings is None:
            self.embeddings = get_embed()

        if self.model is None:
            self.model = create_llm()

    # LOAD VIDEO
    def load_video(self, url: str):
        if not url.strip():
            raise ValueError("YouTube URL cannot be empty.")
        
        video_id = get_video_id(url)
        print( f"Preparing video: {video_id}")

        # Models
        self.initialize_models()

        # PostgreSQL
        self.checkpointer = (self.database.initialize())

        # FAISS
        vectorstore = get_vectorstore(url, self.embeddings)

        # Retriever
        self.retriever = create_retriever( vectorstore)

        # Graph
        self.graph = build_graph(
            self.retriever,
            self.model,
            self.checkpointer
        )

        self.video_id = video_id
        self.video_url = url

        print( f"Video ready: {video_id}")
        return video_id

    # NORMAL CHAT
    def ask(self,question: str,thread_id: str):
        if not question.strip():
            raise ValueError( "Question cannot be empty.")

        if self.graph is None:
            raise ValueError( "Please load a YouTube video first.")

        config = {
            "configurable": {"thread_id": thread_id}
        }

        response = self.graph.invoke(
            {
                "question": question,
                "mode": "chat",
                "messages": [ HumanMessage(content=question)]
            },
            config=config
        )
        return response["answer"]

    # GENERATE MCQs
    def generate_mcqs(
        self,
        number: int,
        difficulty: str,
        thread_id: str
    ):

        if self.graph is None:
            raise ValueError("Please load a YouTube video first.")

        if number < 1 or number > 20:
            raise ValueError("Number of questions must be between 1 and 20.")

        difficulty = difficulty.capitalize()
        if difficulty not in ["Easy", "Medium","Hard" ]:
            raise ValueError( "Difficulty must be Easy, Medium or Hard.")

        config = {
            "configurable": {"thread_id": thread_id}
        }

        response = self.graph.invoke(
            {
                "question": ("Generate important MCQs from the video."),
                "mode": "mcq",
                "number": number,
                "difficulty": difficulty
            }, 
            config=config
        )

        result = response.get("mcqs")
        if result is None:
            raise RuntimeError("MCQ generation failed.")

        return result

    # CLOSE
    def close(self):
        self.database.close()
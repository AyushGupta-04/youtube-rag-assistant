AI YouTube Chatbot
<p align="center"> <strong>Chat with YouTube videos using AI-powered Retrieval-Augmented Generation (RAG)</strong> </p> <p align="center"> <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/LangChain-RAG-1C3C3C?style=for-the-badge" alt="LangChain"> <img src="https://img.shields.io/badge/LangGraph-Workflow-1C3C3C?style=for-the-badge" alt="LangGraph"> <img src="https://img.shields.io/badge/FAISS-Vector%20Search-FF6F00?style=for-the-badge" alt="FAISS"> <img src="https://img.shields.io/badge/Groq-LLM-F55036?style=for-the-badge" alt="Groq"> <img src="https://img.shields.io/badge/PostgreSQL-Memory-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL"> </p> <p align="center"> <a href="#-features">Features</a> • <a href="#-architecture">Architecture</a> • <a href="#-installation">Installation</a> • <a href="#-usage">Usage</a> • <a href="#-project-structure">Project Structure</a> • <a href="#-future-improvements">Future Improvements</a> </p>
📌 Overview
AI YouTube Chatbot is a conversational Retrieval-Augmented Generation (RAG) application that allows users to ask questions about YouTube videos and receive answers based on the video's transcript.

Instead of sending the entire transcript directly to an LLM, the application:

Extracts the YouTube transcript.
Splits the transcript into smaller chunks.
Converts chunks into vector embeddings.
Stores the embeddings in FAISS.
Retrieves the most relevant transcript sections for each question.
Passes the retrieved context to a Groq-powered LLM.
Maintains conversation history using PostgreSQL and LangGraph.
The result is a lightweight, transcript-grounded AI assistant capable of answering questions and handling conversational follow-ups.

✨ Features
Feature	Description
🎬 YouTube Integration	Load transcripts directly from YouTube URLs
🌐 Multi-language	Supports English and Hindi transcript retrieval
✂️ Smart Chunking	Splits transcripts into retrieval-friendly chunks
🧠 Embeddings	Uses BAAI/bge-small-en-v1.5 embeddings
🔎 Semantic Search	Finds transcript sections relevant to user questions
🔀 MMR Retrieval	Improves retrieval diversity and reduces redundant results
💾 FAISS	Stores embeddings locally for fast vector search
♻️ Index Caching	Reuses existing FAISS indexes for previously processed videos
🤖 Groq LLM	Generates fast AI responses using Groq
🔗 LangGraph	Manages the retrieval and generation workflow
💬 Conversational Memory	Supports contextual follow-up questions
🐘 PostgreSQL	Persists LangGraph conversation checkpoints
⚡ Streaming	Supports incremental response generation
🛡️ Grounded Answers	Instructs the model to answer using transcript context only

📑 Table of Contents
📌 Overview
✨ Features
🏗️ Architecture
🔄 RAG Pipeline
1. YouTube URL Processing
2. Transcript Extraction
3. Text Chunking
4. Embedding Generation
5. FAISS Vector Store
6. MMR Retrieval
7. LLM Generation
💬 Conversation Memory
⚡ Streaming
🧰 Tech Stack
📁 Project Structure
🔐 Environment Variables
🚀 Installation
▶️ Usage
🧪 Example
🛡️ Hallucination Control
💾 FAISS Caching
🧩 Core Components
⚠️ Limitations
🔮 Future Improvements
🤝 Contributing
🔒 Security
📄 License
👨‍💻 Author
🏗️ Architecture
The application follows a Retrieval-Augmented Generation architecture.

flowchart TD
    A[🎬 YouTube URL] --> B[Extract Video ID]
    B --> C[📜 Load Transcript]
    C --> D[✂️ Split Transcript]
    D --> E[🧠 Generate Embeddings]
    E --> F[(🔎 FAISS Vector Store)]

    U[👤 User Question] --> R[MMR Retriever]
    F --> R

    R --> G[📚 Relevant Transcript Context]
    G --> H[🔗 LangGraph]

    H --> I[🤖 Groq LLM]
    I --> J[💬 Final Answer]

    M[(🐘 PostgreSQL)] <--> H
    M --> H

🔄 RAG Pipeline
1. YouTube URL Processing
The application accepts a YouTube URL such as:

https://www.youtube.com/watch?v=VIDEO_ID

The video ID is extracted using Python's urllib.parse.

Supported formats include:

https://www.youtube.com/watch?v=VIDEO_ID
https://youtu.be/VIDEO_ID

The extracted video ID is also used to create a unique FAISS index for the video.

2. Transcript Extraction
The application uses YoutubeLoader to retrieve the transcript.

The loader is configured to support:

language=["en", "hi"]

If a transcript cannot be found, the application raises an appropriate error instead of continuing with empty data.

Transcript flow
YouTube URL
     │
     ▼
Video ID
     │
     ▼
YoutubeLoader
     │
     ▼
Transcript Documents

3. Text Chunking
Large transcripts are split into smaller chunks using:

RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)

Configuration
Parameter	Value
Chunk Size	800
Chunk Overlap	150

Chunk overlap helps preserve contextual information between neighboring chunks.

┌──────────────────────────┐
│         Chunk 1          │
└──────────────┬───────────┘
               │ overlap
               ▼
       ┌──────────────────────────┐
       │         Chunk 2          │
       └──────────────┬───────────┘
                      │ overlap
                      ▼
              ┌──────────────────────────┐
              │         Chunk 3          │
              └──────────────────────────┘

4. Embedding Generation
Each transcript chunk is converted into a vector representation using:

BAAI/bge-small-en-v1.5

through:

HuggingFaceEndpointEmbeddings

Conceptually:

Transcript Chunk
       │
       ▼
Embedding Model
       │
       ▼
Numerical Vector

These vectors allow the system to perform semantic similarity searches.

5. FAISS Vector Store
The generated embeddings are stored in FAISS.

Each video receives its own local index:

faiss_indexes/
└── VIDEO_ID/
    ├── index.faiss
    └── index.pkl

This provides two important benefits:

Fast similarity search.
Local caching of processed videos.
6. MMR Retrieval
The application uses Maximum Marginal Relevance (MMR) retrieval:

vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 5,
        "fetch_k": 20
    }
)

Retrieval configuration
Parameter	Value	Purpose
search_type	mmr	Maximum Marginal Relevance
k	5	Number of final documents returned
fetch_k	20	Number of candidate documents considered

MMR attempts to balance:

Relevance
    +
Diversity
    ↓
Better Context

This can help prevent the model from receiving several nearly identical transcript chunks.

7. LLM Generation
After retrieval, the relevant transcript chunks are passed to the LLM.

The project uses:

ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.3
)

The generation pipeline is:

User Question
Retriever
Relevant Documents
Context
Prompt
Groq LLM
Answer
The system prompt explicitly instructs the model to use the retrieved transcript context rather than inventing information.

💬 Conversation Memory
The application uses LangGraph + PostgreSQL for persistent conversation state.

Every conversation is associated with a unique:

thread_id

Example:

config = {
    "configurable": {
        "thread_id": "conversation-1"
    }
}

This allows the assistant to understand follow-up questions.

Example
👤 User:
What is the main topic of the video?

🤖 Assistant:
The video discusses artificial intelligence...

👤 User:
What are the three main points?

🤖 Assistant:
The three main points are...

👤 User:
Can you explain the second one?

🤖 Assistant:
The second point refers to...

The conversation history helps resolve references such as:

"this"
"that"
"the second point"
"explain it again"
"what about the previous point?"
while the transcript remains the factual source.

⚡ Streaming
The project supports streaming through:

ask_stream()

Example:

for chunk in assistant.ask_stream(
    "What is the main idea?",
    thread_id="conversation-1"
):
    print(chunk, end="", flush=True)

Instead of waiting for the entire response, the client can display the answer progressively.

The
 video
 explains
 how
 artificial
 intelligence
 works...

This is particularly useful for building real-time chat interfaces.

🧰 Tech Stack
Technology	Role
🐍 Python	Application development
🦜 LangChain	LLM and RAG components
🔗 LangGraph	Stateful workflow orchestration
🤗 Hugging Face	Embedding generation
🧠 BGE Small EN v1.5	Text embeddings
🔎 FAISS	Vector similarity search
⚡ Groq	LLM inference
🤖 GPT-OSS-20B	Language model
🐘 PostgreSQL	Conversation checkpoint storage
▶️ YouTubeLoader	Transcript extraction

📁 Project Structure
ai-yt-chatbot/
│
├── backend/
│   │
│   ├── config/
│   │   └── settings.py
│   │
│   ├── youtube/
│   │   ├── loader.py
│   │   ├── splitter.py
│   │   └── url.py
│   │
│   ├── vectorstore/
│   │   ├── embeddings.py
│   │   ├── faiss_store.py
│   │   └── retriever.py
│   │
│   ├── llm/
│   │   ├── model.py
│   │   └── prompt.py
│   │
│   ├── graph/
│   │   ├── graph.py
│   │   └── state.py
│   │
│   ├── database/
│   │   └── postgres.py
│   │
│   └── assistant.py
│
├── faiss_indexes/
│   └── <video_id>/
│       ├── index.faiss
│       └── index.pkl
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md

Update the structure above if your actual repository uses different filenames or folders.

🔐 Environment Variables
Create a .env file in the project root.

HF_TOKEN=your_huggingface_token
GROQ_API_KEY=your_groq_api_key
POSTGRES_URL=your_postgresql_connection_string

Variables
Variable	Required	Description
HF_TOKEN	✅	Hugging Face authentication token
GROQ_API_KEY	✅	Groq API key
POSTGRES_URL	✅	PostgreSQL connection string

Example:

POSTGRES_URL=postgresql://username:password@localhost:5432/youtube_chat

⚠️ Never commit .env to GitHub.

🚀 Installation
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/ai-yt-chatbot.git

cd ai-yt-chatbot

Replace YOUR_USERNAME with your GitHub username.

2. Create a virtual environment
Windows
python -m venv venv

venv\Scripts\activate

Linux / macOS
python3 -m venv venv

source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Configure environment variables
Create:

.env

Add:

HF_TOKEN=your_huggingface_token
GROQ_API_KEY=your_groq_api_key
POSTGRES_URL=your_postgresql_connection_string

5. Configure PostgreSQL
Make sure PostgreSQL is running and the database specified in POSTGRES_URL exists.

The application initializes the LangGraph PostgreSQL checkpointer through:

PostgresSaver.from_conn_string(POSTGRES_URL)

▶️ Usage
Import the assistant:

from backend.assistant import YouTubeAssistant

Create the assistant:

assistant = YouTubeAssistant()

Load a YouTube video:

assistant.load_video(
    "https://www.youtube.com/watch?v=VIDEO_ID"
)

Ask a question:

answer = assistant.ask(
    "What is the main topic of this video?",
    thread_id="conversation-1"
)

print(answer)

⚡ Streaming Usage
for chunk in assistant.ask_stream(
    "Explain the main topic.",
    thread_id="conversation-1"
):
    print(chunk, end="", flush=True)

🧹 Closing the Assistant
When the application is finished, close the PostgreSQL connection:

assistant.close()

🧪 Example
Input
YouTube URL:
https://www.youtube.com/watch?v=VIDEO_ID

Question
What are the main points discussed in the video?

Processing
Question
   ↓
Embedding / Retrieval
   ↓
FAISS
   ↓
Top Relevant Chunks
   ↓
LangGraph
   ↓
Groq LLM
   ↓
Answer

Follow-up
User:
Can you explain the second point in more detail?

The existing conversation history allows the chatbot to understand what "second point" refers to.

🛡️ Hallucination Control
The system prompt contains the following core instruction:

Answer ONLY using the provided video transcript context.

If the requested information is not available in the provided context, the model is instructed to return:

The video doesn't mention this

Grounding strategy
Yes
No
User Question
Retriever
Relevant Transcript?
Provide Context to LLM
Generate Grounded Answer
The video doesn't mention this
This approach reduces the likelihood of the model answering from unrelated general knowledge.

Note: RAG cannot guarantee zero hallucinations. The final response still depends on transcript quality, retrieval quality, prompt adherence, and model behavior.

💾 FAISS Caching
The application avoids repeatedly processing the same video.

First request
YouTube URL
     ↓
Extract Video ID
     ↓
Load Transcript
     ↓
Chunk Transcript
     ↓
Generate Embeddings
     ↓
Create FAISS
     ↓
Save FAISS

Subsequent request
YouTube URL
     ↓
Extract Video ID
     ↓
Check FAISS Index
     ↓
Index Exists
     ↓
Load Existing FAISS

The index is stored using:

faiss_indexes/<video_id>/

This can significantly reduce repeated transcript processing and embedding calls.

🧩 Core Components
Component	Responsibility
get_video_id()	Extracts the YouTube video ID
yt_loader()	Retrieves the YouTube transcript
get_chunk()	Splits transcript into chunks
get_embed()	Initializes Hugging Face embeddings
get_vectorstore()	Creates or loads FAISS
create_retriever()	Creates the MMR retriever
create_llm()	Initializes the Groq LLM
build_graph()	Creates the LangGraph workflow
Database	Manages PostgreSQL checkpointer
YouTubeAssistant	Main application interface

🧠 LangGraph State
The chatbot maintains a structured state:

class YTChatState(TypedDict):
    question: str
    context: str
    answer: str
    documents: list[Document]
    citations: List[Citation]
    messages: Annotated[List[BaseMessage], add_messages]

This allows the graph to pass:

User questions
Retrieved context
Documents
Generated answers
Conversation messages
Citation information
between workflow nodes.

🔄 LangGraph Workflow
The current workflow is intentionally simple:

[START]
Retrieve Node
Generate Node
[END]
Retrieve Node
Question
   ↓
Retriever
   ↓
Relevant Documents
   ↓
Context

Generate Node
Context
   +
Conversation History
   +
Question
   ↓
Prompt
   ↓
Groq LLM
   ↓
Answer

⚠️ Limitations
Current limitations include:

YouTube transcripts must be available.
Transcript retrieval depends on YouTube availability and configuration.
Current language configuration focuses on English and Hindi.
FAISS indexes are stored locally.
PostgreSQL is required for persistent conversation state.
Retrieval quality depends on chunk size, embeddings, and query quality.
Timestamp citation data is defined in the state but is not yet fully surfaced in generated responses.
The current LangGraph workflow contains only retrieval and generation nodes.
No frontend is included in the core implementation.
🔮 Future Improvements
The project can be extended with:

 🌐 FastAPI backend
 🎨 React / Next.js frontend
 🔐 User authentication
 👥 Multi-user support
 🎬 Multiple videos per conversation
 🌍 Automatic language detection
 🗣️ More transcript languages
 ⏱️ Clickable timestamp citations
 📚 Source citations in answers
 🔎 Hybrid keyword + semantic retrieval
 🧠 Reranking models
 ✍️ Query rewriting
 🐳 Docker support
 🧪 Automated tests
 🚀 GitHub Actions CI/CD
 📊 RAG evaluation metrics
 🔭 LangSmith observability
 📈 Retrieval and answer-quality analytics
🤝 Contributing
Contributions are welcome!

Fork the repository
Click the Fork button on GitHub.

Clone your fork
git clone https://github.com/YOUR_USERNAME/ai-yt-chatbot.git

cd ai-yt-chatbot

Create a branch
git checkout -b feature/your-feature

Make your changes
Implement your feature or fix.

Commit
git add .

git commit -m "Add your feature"

Push
git push origin feature/your-feature

Then open a Pull Request on GitHub.

🔒 Security
Make sure .gitignore contains:

.env
venv/
__pycache__/
*.pyc
faiss_indexes/

Never commit:

❌ API keys
❌ Passwords
❌ .env files
❌ PostgreSQL credentials
❌ Private tokens
❌ Other sensitive information
If a secret is accidentally pushed to GitHub, revoke or rotate it immediately.

Deleting the file afterward does not remove the secret from Git history.

📄 License
This project is licensed under the MIT License.

Add a LICENSE file to the root of the repository containing the MIT License text.

🙏 Acknowledgements
This project was built using:

LangChain
LangGraph
Hugging Face
FAISS
Groq
PostgreSQL

👨‍💻 Author
AYUSH GUPTA

Built with Python, LangChain, LangGraph, FAISS, Groq, Hugging Face, and PostgreSQL.

If you found this project useful, consider giving it a ⭐ on GitHub!
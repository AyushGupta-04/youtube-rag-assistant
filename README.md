# 🎥 AI YouTube Chatbot

<p align="center">
  <strong>Chat with YouTube videos using AI-powered Retrieval-Augmented Generation (RAG)</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/LangChain-RAG-1C3C3C?style=for-the-badge" alt="LangChain">
  <img src="https://img.shields.io/badge/LangGraph-Workflow-1C3C3C?style=for-the-badge" alt="LangGraph">
  <img src="https://img.shields.io/badge/FAISS-Vector_Search-FF6F00?style=for-the-badge" alt="FAISS">
  <img src="https://img.shields.io/badge/Groq-LLM-F55036?style=for-the-badge" alt="Groq">
  <img src="https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
</p>

<p align="center">
  <a href="#-overview">Overview</a> •
  <a href="#-features">Features</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-usage">Usage</a>
</p>

---

## 📑 Table of Contents

<table>
  <tr>
    <th>#</th>
    <th>Topic</th>
  </tr>
  <tr>
    <td>1</td>
    <td><a href="#-overview">📌 Overview</a></td>
  </tr>
  <tr>
    <td>2</td>
    <td><a href="#-features">✨ Features</a></td>
  </tr>
  <tr>
    <td>3</td>
    <td><a href="#-architecture">🏗️ Architecture</a></td>
  </tr>
  <tr>
    <td>4</td>
    <td><a href="#-rag-pipeline">🔄 RAG Pipeline</a></td>
  </tr>
  <tr>
    <td>5</td>
    <td><a href="#-youtube-url-processing">🎬 YouTube URL Processing</a></td>
  </tr>
  <tr>
    <td>6</td>
    <td><a href="#-transcript-extraction">📜 Transcript Extraction</a></td>
  </tr>
  <tr>
    <td>7</td>
    <td><a href="#-text-chunking">✂️ Text Chunking</a></td>
  </tr>
  <tr>
    <td>8</td>
    <td><a href="#-embedding-generation">🧠 Embedding Generation</a></td>
  </tr>
  <tr>
    <td>9</td>
    <td><a href="#-faiss-vector-store">💾 FAISS Vector Store</a></td>
  </tr>
  <tr>
    <td>10</td>
    <td><a href="#-mmr-retrieval">🔎 MMR Retrieval</a></td>
  </tr>
  <tr>
    <td>11</td>
    <td><a href="#-llm-generation">🤖 LLM Generation</a></td>
  </tr>
  <tr>
    <td>12</td>
    <td><a href="#-conversation-memory">💬 Conversation Memory</a></td>
  </tr>
  <tr>
    <td>13</td>
    <td><a href="#-streaming">⚡ Streaming</a></td>
  </tr>
  <tr>
    <td>14</td>
    <td><a href="#-tech-stack">🧰 Tech Stack</a></td>
  </tr>
  <tr>
    <td>15</td>
    <td><a href="#-project-structure">📁 Project Structure</a></td>
  </tr>
  <tr>
    <td>16</td>
    <td><a href="#-environment-variables">🔐 Environment Variables</a></td>
  </tr>
  <tr>
    <td>17</td>
    <td><a href="#-installation">🚀 Installation</a></td>
  </tr>
  <tr>
    <td>18</td>
    <td><a href="#-usage">▶️ Usage</a></td>
  </tr>
  <tr>
    <td>19</td>
    <td><a href="#-example">🧪 Example</a></td>
  </tr>
  <tr>
    <td>20</td>
    <td><a href="#-hallucination-control">🛡️ Hallucination Control</a></td>
  </tr>
  <tr>
    <td>21</td>
    <td><a href="#-faiss-caching">♻️ FAISS Caching</a></td>
  </tr>
  <tr>
    <td>22</td>
    <td><a href="#-core-components">🧩 Core Components</a></td>
  </tr>
  <tr>
    <td>23</td>
    <td><a href="#-langgraph-state">🧠 LangGraph State</a></td>
  </tr>
  <tr>
    <td>24</td>
    <td><a href="#-langgraph-workflow">🔗 LangGraph Workflow</a></td>
  </tr>
  <tr>
    <td>25</td>
    <td><a href="#-limitations">⚠️ Limitations</a></td>
  </tr>
  <tr>
    <td>26</td>
    <td><a href="#-future-improvements">🔮 Future Improvements</a></td>
  </tr>
  <tr>
    <td>27</td>
    <td><a href="#-contributing">🤝 Contributing</a></td>
  </tr>
  <tr>
    <td>28</td>
    <td><a href="#-security">🔒 Security</a></td>
  </tr>
  <tr>
    <td>29</td>
    <td><a href="#-license">📄 License</a></td>
  </tr>
  <tr>
    <td>30</td>
    <td><a href="#-acknowledgements">🙏 Acknowledgements</a></td>
  </tr>
  <tr>
    <td>31</td>
    <td><a href="#-author">👨‍💻 Author</a></td>
  </tr>
</table>

---

## 📌 Overview

**AI YouTube Chatbot** is a conversational **Retrieval-Augmented Generation (RAG)** application that allows users to ask questions about YouTube videos and receive answers based on the video's transcript.

Instead of sending the entire transcript directly to an LLM, the application:

- Extracts the YouTube transcript.
- Splits the transcript into smaller chunks.
- Converts chunks into vector embeddings.
- Stores embeddings in FAISS.
- Retrieves the most relevant transcript sections.
- Passes the retrieved context to a Groq-powered LLM.
- Maintains conversation history using LangGraph and PostgreSQL.

The result is a lightweight, transcript-grounded AI assistant capable of answering questions and handling conversational follow-ups.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎬 YouTube Integration | Load transcripts directly from YouTube URLs |
| 🌐 Multi-language | Supports English and Hindi transcript retrieval |
| ✂️ Smart Chunking | Splits transcripts into retrieval-friendly chunks |
| 🧠 Embeddings | Uses `BAAI/bge-small-en-v1.5` |
| 🔎 Semantic Search | Finds transcript sections relevant to user questions |
| 🔀 MMR Retrieval | Improves retrieval diversity and reduces redundant results |
| 💾 FAISS | Stores embeddings locally for fast vector search |
| ♻️ Index Caching | Reuses existing FAISS indexes for previously processed videos |
| 🤖 Groq LLM | Generates fast AI responses using Groq |
| 🔗 LangGraph | Manages the retrieval and generation workflow |
| 💬 Conversational Memory | Supports contextual follow-up questions |
| 🐘 PostgreSQL | Persists LangGraph conversation checkpoints |
| ⚡ Streaming | Supports incremental response generation |
| 🛡️ Grounded Answers | Instructs the model to answer using transcript context only |

---

## 🏗️ Architecture

The application follows a Retrieval-Augmented Generation architecture.

```mermaid
flowchart TD
    A["🎬 YouTube URL"] --> B["Extract Video ID"]
    B --> C["📜 Load Transcript"]
    C --> D["✂️ Split Transcript"]
    D --> E["🧠 Generate Embeddings"]
    E --> F[("🔎 FAISS Vector Store")]

    U["👤 User Question"] --> R["🔀 MMR Retriever"]
    F --> R

    R --> G["📚 Relevant Transcript Context"]
    G --> H["🔗 LangGraph"]

    H --> I["🤖 Groq LLM"]
    I --> J["💬 Final Answer"]

    M[("🐘 PostgreSQL")] <--> H
```

### High-Level Flow

```text
YouTube Video
      ↓
Transcript
      ↓
Text Chunking
      ↓
Embeddings
      ↓
FAISS
      ↓
MMR Retrieval
      ↓
Relevant Context
      ↓
Groq LLM
      ↓
Answer
```

---

# 🔄 RAG Pipeline

## 🎬 YouTube URL Processing

The application accepts common YouTube URL formats.

### Standard YouTube URL

```text
https://www.youtube.com/watch?v=VIDEO_ID
```

### Short YouTube URL

```text
https://youtu.be/VIDEO_ID
```

The video ID is extracted using Python's `urllib.parse`.

The extracted video ID is also used to create a unique FAISS index for the video.

---

## 📜 Transcript Extraction

The application uses `YoutubeLoader` to retrieve the YouTube transcript.

The loader is configured to support:

```python
language=["en", "hi"]
```

If a transcript cannot be found, the application raises an error instead of continuing with empty data.

### Transcript Flow

```text
YouTube URL
     ↓
Video ID
     ↓
YoutubeLoader
     ↓
Transcript Documents
```

---

## ✂️ Text Chunking

Large transcripts are split into smaller chunks using:

```python
RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)
```

### Configuration

| Parameter | Value |
|---|---:|
| Chunk Size | `800` |
| Chunk Overlap | `150` |

Chunk overlap helps preserve contextual information between neighboring chunks.

```text
┌──────────────────────────┐
│        Chunk 1           │
└────────────┬─────────────┘
             │
             │ overlap
             ▼
┌──────────────────────────┐
│        Chunk 2           │
└────────────┬─────────────┘
             │
             │ overlap
             ▼
┌──────────────────────────┐
│        Chunk 3           │
└──────────────────────────┘
```

---

## 🧠 Embedding Generation

Each transcript chunk is converted into a vector representation using:

```text
BAAI/bge-small-en-v1.5
```

through:

```python
HuggingFaceEndpointEmbeddings
```

### Embedding Flow

```text
Transcript Chunk
       ↓
Embedding Model
       ↓
Numerical Vector
```

These vectors allow the system to perform semantic similarity searches.

---

## 💾 FAISS Vector Store

The generated embeddings are stored in **FAISS**.

Each video receives its own local index:

```text
faiss_indexes/
└── VIDEO_ID/
    ├── index.faiss
    └── index.pkl
```

This provides two important benefits:

- Fast similarity search.
- Local caching of processed videos.

---

## 🔎 MMR Retrieval

The application uses **Maximum Marginal Relevance (MMR)** retrieval:

```python
vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 5,
        "fetch_k": 20
    }
)
```

### Retrieval Configuration

| Parameter | Value | Purpose |
|---|---:|---|
| `search_type` | `mmr` | Maximum Marginal Relevance |
| `k` | `5` | Number of final documents returned |
| `fetch_k` | `20` | Number of candidate documents considered |

MMR attempts to balance:

```text
Relevance
    +
Diversity
    ↓
Better Context
```

This can help prevent the model from receiving several nearly identical transcript chunks.

---

## 🤖 LLM Generation

After retrieval, the relevant transcript chunks are passed to the LLM.

The project uses:

```python
ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.3
)
```

### Generation Pipeline

```text
User Question
      ↓
Retriever
      ↓
Relevant Documents
      ↓
Context
      ↓
Prompt
      ↓
Groq LLM
      ↓
Answer
```

The system prompt explicitly instructs the model to use the retrieved transcript context rather than inventing information.

---

## 💬 Conversation Memory

The application uses **LangGraph + PostgreSQL** for persistent conversation state.

Every conversation is associated with a unique:

```text
thread_id
```

Example:

```python
config = {
    "configurable": {
        "thread_id": "conversation-1"
    }
}
```

This allows the assistant to understand follow-up questions.

### Example Conversation

```text
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
```

The conversation history helps resolve references such as:

- "this"
- "that"
- "the second point"
- "explain it again"
- "what about the previous point?"

The transcript remains the factual source.

---

## ⚡ Streaming

The project supports streaming through:

```python
ask_stream()
```

### Example

```python
for chunk in assistant.ask_stream(
    "What is the main idea?",
    thread_id="conversation-1"
):
    print(chunk, end="", flush=True)
```

Instead of waiting for the entire response, the client can display the answer progressively.

This is particularly useful for building real-time chat interfaces.

---

## 🧰 Tech Stack

| Technology | Role |
|---|---|
| 🐍 Python | Application development |
| 🦜 LangChain | LLM and RAG components |
| 🔗 LangGraph | Stateful workflow orchestration |
| 🤗 Hugging Face | Embedding generation |
| 🧠 BGE Small EN v1.5 | Text embeddings |
| 🔎 FAISS | Vector similarity search |
| ⚡ Groq | LLM inference |
| 🤖 GPT-OSS-20B | Language model |
| 🐘 PostgreSQL | Conversation checkpoint storage |
| ▶️ YoutubeLoader | Transcript extraction |

---

## 📁 Project Structure

```text
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
```

> Update the structure above if your actual repository uses different filenames or folders.

---

## 🔐 Environment Variables

Create a `.env` file in the project root.

```env
HF_TOKEN=your_huggingface_token
GROQ_API_KEY=your_groq_api_key
POSTGRES_URL=your_postgresql_connection_string
```

### Variables

| Variable | Required | Description |
|---|:---:|---|
| `HF_TOKEN` | ✅ | Hugging Face authentication token |
| `GROQ_API_KEY` | ✅ | Groq API key |
| `POSTGRES_URL` | ✅ | PostgreSQL connection string |

### Example

```env
POSTGRES_URL=postgresql://username:password@localhost:5432/youtube_chat
```

> ⚠️ **Never commit `.env` to GitHub.**

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-yt-chatbot.git
cd ai-yt-chatbot
```

Replace `YOUR_USERNAME` with your GitHub username.

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create:

```text
.env
```

Add:

```env
HF_TOKEN=your_huggingface_token
GROQ_API_KEY=your_groq_api_key
POSTGRES_URL=your_postgresql_connection_string
```

---

## 5. Configure PostgreSQL

Make sure PostgreSQL is running and the database specified in `POSTGRES_URL` exists.

The application initializes the LangGraph PostgreSQL checkpointer through:

```python
PostgresSaver.from_conn_string(POSTGRES_URL)
```

---

# ▶️ Usage

## Import the Assistant

```python
from backend.assistant import YouTubeAssistant
```

## Create the Assistant

```python
assistant = YouTubeAssistant()
```

## Load a YouTube Video

```python
assistant.load_video(
    "https://www.youtube.com/watch?v=VIDEO_ID"
)
```

## Ask a Question

```python
answer = assistant.ask(
    "What is the main topic of this video?",
    thread_id="conversation-1"
)

print(answer)
```

---

## ⚡ Streaming Usage

```python
for chunk in assistant.ask_stream(
    "Explain the main topic.",
    thread_id="conversation-1"
):
    print(chunk, end="", flush=True)
```

---

## 🧹 Closing the Assistant

When the application is finished, close the PostgreSQL connection:

```python
assistant.close()
```

---

# 🧪 Example

### Input

```text
YouTube URL:
https://www.youtube.com/watch?v=VIDEO_ID
```

### Question

```text
What are the main points discussed in the video?
```

### Processing

```text
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
```

### Follow-up

```text
👤 User:
Can you explain the second point in more detail?
```

The existing conversation history allows the chatbot to understand what "second point" refers to.

---

# 🛡️ Hallucination Control

The system prompt contains the following core instruction:

```text
Answer ONLY using the provided video transcript context.
```

If the requested information is not available in the provided context, the model is instructed to return:

```text
The video doesn't mention this
```

### Grounding Strategy

```mermaid
flowchart TD
    A["👤 User Question"] --> B["🔎 Retriever"]
    B --> C{"Relevant Transcript?"}

    C -->|Yes| D["📚 Provide Context to LLM"]
    D --> E["🤖 Generate Grounded Answer"]

    C -->|No| F["The video doesn't mention this"]
```

This approach reduces the likelihood of the model answering from unrelated general knowledge.

> **Note:** RAG cannot guarantee zero hallucinations. The final response still depends on transcript quality, retrieval quality, prompt adherence, and model behavior.

---

# ♻️ FAISS Caching

The application avoids repeatedly processing the same video.

### First Request

```text
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
```

### Subsequent Request

```text
YouTube URL
     ↓
Extract Video ID
     ↓
Check FAISS Index
     ↓
Index Exists
     ↓
Load Existing FAISS
```

The index is stored using:

```text
faiss_indexes/<video_id>/
```

This can significantly reduce repeated transcript processing and embedding calls.

---

# 🧩 Core Components

| Component | Responsibility |
|---|---|
| `get_video_id()` | Extracts the YouTube video ID |
| `yt_loader()` | Retrieves the YouTube transcript |
| `get_chunk()` | Splits transcript into chunks |
| `get_embed()` | Initializes Hugging Face embeddings |
| `get_vectorstore()` | Creates or loads FAISS |
| `create_retriever()` | Creates the MMR retriever |
| `create_llm()` | Initializes the Groq LLM |
| `build_graph()` | Creates the LangGraph workflow |
| `Database` | Manages PostgreSQL checkpointer |
| `YouTubeAssistant` | Main application interface |

---

# 🧠 LangGraph State

The chatbot maintains a structured state:

```python
class YTChatState(TypedDict):
    question: str
    context: str
    answer: str
    documents: list[Document]
    citations: List[Citation]
    messages: Annotated[List[BaseMessage], add_messages]
```

This allows the graph to pass:

- User questions
- Retrieved context
- Documents
- Generated answers
- Conversation messages
- Citation information

between workflow nodes.

---

# 🔗 LangGraph Workflow

The current workflow is intentionally simple:

```mermaid
flowchart LR
    START(["START"])
    RETRIEVE["🔎 Retrieve Node"]
    GENERATE["🤖 Generate Node"]
    END_NODE(["END"])

    START --> RETRIEVE
    RETRIEVE --> GENERATE
    GENERATE --> END_NODE
```

### Retrieve Node

```text
Question
   ↓
Retriever
   ↓
Relevant Documents
   ↓
Context
```

The retrieve node searches the FAISS vector store and prepares the transcript context.

### Generate Node

```text
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
```

The generate node creates the final response using the retrieved context and conversation history.

---

# ⚠️ Limitations

Current limitations include:

- YouTube transcripts must be available.
- Transcript retrieval depends on YouTube availability and configuration.
- Current language configuration focuses on English and Hindi.
- FAISS indexes are stored locally.
- PostgreSQL is required for persistent conversation state.
- Retrieval quality depends on chunk size, embeddings, and query quality.
- Timestamp citation data is defined in the state but is not yet fully surfaced in generated responses.
- The current LangGraph workflow contains only retrieval and generation nodes.
- No frontend is included in the core implementation.

---

# 🔮 Future Improvements

The project can be extended with:

- [ ] 🌐 FastAPI backend
- [ ] 🎨 React / Next.js frontend
- [ ] 🔐 User authentication
- [ ] 👥 Multi-user support
- [ ] 🎬 Multiple videos per conversation
- [ ] 🌍 Automatic language detection
- [ ] 🗣️ More transcript languages
- [ ] ⏱️ Clickable timestamp citations
- [ ] 📚 Source citations in answers
- [ ] 🔎 Hybrid keyword + semantic retrieval
- [ ] 🧠 Reranking models
- [ ] ✍️ Query rewriting
- [ ] 🐳 Docker support
- [ ] 🧪 Automated tests
- [ ] 🚀 GitHub Actions CI/CD
- [ ] 📊 RAG evaluation metrics
- [ ] 🔭 LangSmith observability
- [ ] 📈 Retrieval and answer-quality analytics

---

# 🤝 Contributing

Contributions are welcome!

## 1. Fork the Repository

Click the **Fork** button on GitHub.

## 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/ai-yt-chatbot.git
cd ai-yt-chatbot
```

## 3. Create a Feature Branch

```bash
git checkout -b feature/your-feature
```

## 4. Make Your Changes

Implement your feature or fix.

## 5. Commit Your Changes

```bash
git add .
git commit -m "Add your feature"
```

## 6. Push Your Branch

```bash
git push origin feature/your-feature
```

Then open a Pull Request on GitHub.

---

# 🔒 Security

Make sure `.gitignore` contains:

```gitignore
.env
venv/
__pycache__/
*.pyc
faiss_indexes/
```

Never commit:

- ❌ API keys
- ❌ Passwords
- ❌ `.env` files
- ❌ PostgreSQL credentials
- ❌ Private tokens
- ❌ Other sensitive information

If a secret is accidentally pushed to GitHub, revoke or rotate it immediately.

> Deleting the file afterward does not remove the secret from Git history.

---

# 📄 License

This project is licensed under the **MIT License**.

Add a `LICENSE` file to the root of the repository containing the MIT License text.

---

# 🙏 Acknowledgements

This project was built using:

- [LangChain](https://www.langchain.com/)
- [LangGraph](https://www.langchain.com/langgraph)
- [Hugging Face](https://huggingface.co/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Groq](https://groq.com/)
- [PostgreSQL](https://www.postgresql.org/)

---

# 👨‍💻 Author

## AYUSH GUPTA

Built with:

**Python • LangChain • LangGraph • FAISS • Groq • Hugging Face • PostgreSQL**

If you found this project useful, consider giving the repository a ⭐ on GitHub!

---

## ⬆️ Back to Top

<p align="center">
  <a href="#-ai-youtube-chatbot">⬆️ Back to Top</a>
</p>

# 🎥 AI YouTube Chatbot

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/LangChain-RAG-1C3C3C?style=for-the-badge">
  <img src="https://img.shields.io/badge/LangGraph-Workflow-1C3C3C?style=for-the-badge">
  <img src="https://img.shields.io/badge/FAISS-Vector_Search-FF6F00?style=for-the-badge">
  <img src="https://img.shields.io/badge/Groq-LLM-F55036?style=for-the-badge">
  <img src="https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/ReportLab-PDF-B22222?style=for-the-badge">
</p>

<p align="center">
  <strong>Chat with YouTube videos. Ask questions. Generate quizzes. Learn faster.</strong>
</p>

<p align="center">
  An AI-powered YouTube learning assistant built with
  <strong>RAG, LangGraph, FAISS, Groq, PostgreSQL, and Streamlit.</strong>
</p>

<p align="center">
  <a href="#-overview">Overview</a> •
  <a href="#-features">Features</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-rag-pipeline">RAG Pipeline</a> •
  <a href="#-mcq-system">MCQ System</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-usage">Usage</a>
</p>

---

## 📌 Overview

**AI YouTube Chatbot** transforms YouTube videos into an interactive learning experience.

Instead of manually searching through a video's transcript, users can load a YouTube video and interact with its content using natural language.

The application uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant transcript sections before generating grounded answers.

It also includes an integrated **MCQ generation and interactive quiz system**, allowing users to turn video content into structured quizzes and download them as PDFs.

### 🎯 What It Can Do

- 🎬 Load YouTube videos
- 📜 Extract English and Hindi transcripts
- ✂️ Split transcripts into retrieval-friendly chunks
- 🧠 Generate semantic embeddings
- 🔎 Search transcript content using MMR retrieval
- 🤖 Generate grounded answers using Groq
- 💬 Maintain conversational context
- 📝 Generate transcript-grounded MCQs
- 🎚️ Choose Easy, Medium, or Hard difficulty
- 🎯 Take interactive quizzes
- 📊 Calculate quiz scores
- 💡 Review explanations
- 📄 Export quizzes as PDF
- 💾 Cache FAISS indexes for faster future requests
- 🐘 Persist LangGraph conversation checkpoints with PostgreSQL
- 💬 Maintain multiple independent chat sessions

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎬 YouTube Integration | Load transcripts directly from YouTube URLs |
| 🌐 Multi-language | Supports English and Hindi transcript retrieval |
| ✂️ Smart Chunking | Splits transcripts into retrieval-friendly chunks |
| 🧠 Embeddings | Uses `BAAI/bge-small-en-v1.5` |
| 🔎 Semantic Search | Finds transcript sections relevant to questions |
| 🔀 MMR Retrieval | Improves retrieval diversity and reduces redundancy |
| 💾 FAISS Vector Store | Stores embeddings locally for fast search |
| ♻️ FAISS Caching | Reuses indexes for previously processed videos |
| 🤖 Groq LLM | Generates fast AI responses |
| 🔗 LangGraph | Manages chat and MCQ workflows |
| 💬 Conversation Memory | Supports contextual follow-up questions |
| 🐘 PostgreSQL | Persists LangGraph conversation checkpoints |
| 📝 MCQ Generation | Generates transcript-grounded MCQs |
| 🎚️ Difficulty Selection | Easy, Medium, and Hard |
| 🔢 Question Control | Generate 1–20 questions |
| 🎯 Interactive Quiz | Select answers and submit the quiz |
| 📊 Score Calculation | Automatically calculates scores |
| 💡 Explanations | Shows explanations for generated questions |
| 📄 PDF Export | Downloads quizzes as PDF files |
| 💬 Multiple Chats | Supports independent chat sessions |
| 🎥 Video Per Chat | Each chat can maintain its own video |
| 🛡️ Grounded Answers | Answers rely on retrieved transcript context |

---

## 🏗️ Architecture

```mermaid
flowchart TD
    A["🎬 YouTube URL"] --> B["🔍 Extract Video ID"]
    B --> C["📜 Load Transcript"]
    C --> D["✂️ Split Transcript"]
    D --> E["🧠 Generate Embeddings"]
    E --> F[("💾 FAISS Vector Store")]

    U["👤 User"] --> Q["❓ Question"]
    Q --> R["🔀 MMR Retriever"]
    F --> R

    R --> G["📚 Relevant Transcript Context"]
    G --> H["🔗 LangGraph"]

    H --> I{"⚙️ Select Mode"}

    I -->|Chat| J["💬 Chat Node"]
    I -->|MCQ| K["📝 MCQ Node"]

    J --> L["🤖 Groq LLM"]
    L --> M["💡 Grounded Answer"]

    K --> N["📦 Structured MCQResponse"]
    N --> O["🎯 Interactive Quiz"]
    O --> P["📊 Score"]

    N --> S["📄 ReportLab"]
    S --> T["⬇️ PDF Download"]

    DB[("🐘 PostgreSQL")]
    DB <--> H
```

---

## 🔄 Complete Application Flow

```text
                    🎬 YouTube Video
                           │
                           ▼
                   🔍 Extract Video ID
                           │
                           ▼
                    📜 Transcript
                           │
                           ▼
                    ✂️ Text Chunking
                           │
                           ▼
                  🧠 Embedding Model
                           │
                           ▼
                  💾 FAISS Vector Store
                           │
                           ▼
                    🔎 MMR Retrieval
                           │
                           ▼
                 📚 Relevant Context
                           │
                           ▼
                     🔗 LangGraph
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
         💬 Chat Mode              📝 MCQ Mode
              │                         │
              ▼                         ▼
         🤖 Groq LLM             Structured Output
              │                         │
              ▼                         ▼
       💡 Grounded Answer          🎯 Interactive Quiz
                                        │
                                        ▼
                                   📊 Score
                                        │
                                        ▼
                                  📄 PDF Export
```

---

## 🔄 RAG Pipeline

```mermaid
flowchart LR
    A["🎬 YouTube URL"]
    B["📜 Transcript"]
    C["✂️ Chunking"]
    D["🧠 Embeddings"]
    E["💾 FAISS"]
    F["🔎 MMR Retriever"]
    G["📚 Context"]
    H["🤖 Groq"]
    I["💡 Answer"]

    A --> B --> C --> D --> E
    E --> F --> G --> H --> I
```

### RAG Process

```text
YouTube URL
     ↓
Transcript Extraction
     ↓
Text Chunking
     ↓
Embedding Generation
     ↓
FAISS Vector Store
     ↓
MMR Retrieval
     ↓
Relevant Transcript Context
     ↓
Groq LLM
     ↓
Grounded Answer
```

---

## 🎬 YouTube URL Processing

The application supports common YouTube URL formats.

### Standard URL

```text
https://www.youtube.com/watch?v=VIDEO_ID
```

### Short URL

```text
https://youtu.be/VIDEO_ID
```

The video ID is extracted using:

```python
get_video_id()
```

The extracted video ID is also used to identify the corresponding FAISS index.

---

## 📜 Transcript Extraction

The application retrieves YouTube transcripts through the existing loader pipeline.

The loader supports:

```python
language=["en", "hi"]
```

### Transcript Flow

```text
YouTube URL
     ↓
Video ID
     ↓
YoutubeLoader
     ↓
Transcript Documents
     ↓
Text Processing
```

If a transcript cannot be found, the application raises an error rather than continuing with empty data.

---

## ✂️ Text Chunking

Large transcripts are split using:

```python
RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)
```

| Parameter | Value |
|---|---:|
| Chunk Size | 800 |
| Chunk Overlap | 150 |

```text
┌──────────────────────────┐
│        CHUNK 1           │
└────────────┬─────────────┘
             │
             │ overlap
             ▼
┌──────────────────────────┐
│        CHUNK 2           │
└────────────┬─────────────┘
             │
             │ overlap
             ▼
┌──────────────────────────┐
│        CHUNK 3           │
└──────────────────────────┘
```

Chunk overlap helps preserve contextual information between neighboring chunks.

---

## 🧠 Embedding Generation

Each transcript chunk is converted into a vector using:

```text
BAAI/bge-small-en-v1.5
```

### Flow

```text
Transcript Chunk
       ↓
Embedding Model
       ↓
Numerical Vector
       ↓
FAISS
```

---

## 💾 FAISS Vector Store

Each video receives its own local index:

```text
faiss_indexes/
└── VIDEO_ID/
    ├── index.faiss
    └── index.pkl
```

Benefits:

- ⚡ Fast similarity search
- 💾 Local storage
- ♻️ Reuse of processed videos
- 🚀 Faster future requests

The `YouTubeAssistant.load_video()` method loads or creates the FAISS vector store and creates the retriever.

---

## 🔎 MMR Retrieval

The application uses Maximum Marginal Relevance retrieval:

```python
vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 5,
        "fetch_k": 20
    }
)
```

| Parameter | Value | Purpose |
|---|---:|---|
| `search_type` | `mmr` | Maximum Marginal Relevance |
| `k` | `5` | Final documents returned |
| `fetch_k` | `20` | Candidate documents |

MMR balances:

```text
Relevance
    +
Diversity
    ↓
Better Context
```

---

## 🤖 LLM Generation

The LLM is initialized using:

```python
create_llm()
```

The application uses a Groq-powered model.

```text
👤 User Question
       ↓
🔎 Retriever
       ↓
📚 Relevant Documents
       ↓
🧩 Context
       ↓
📝 Prompt
       ↓
🤖 Groq LLM
       ↓
💡 Final Answer
```

The system prompt instructs the model to rely only on the retrieved transcript context.

---

## 💬 Conversation Memory

The application uses **LangGraph + PostgreSQL** for conversation checkpoints.

Every conversation has a unique:

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

A new Streamlit chat uses:

```python
first_chat_id = str(uuid.uuid4())
```

Each chat can maintain:

```text
title
thread_id
video_url
video_id
messages
mcqs
quiz_submitted
score
```

### Example

```text
👤 User:
What is the main topic?

🤖 Assistant:
The video discusses artificial intelligence...

👤 User:
What are the three main points?

🤖 Assistant:
The three main points are...

👤 User:
Explain the second one.

🤖 Assistant:
The second point refers to...
```

Conversation history helps resolve references such as:

- "this"
- "that"
- "the second point"
- "explain it again"
- "what about the previous point?"

The transcript remains the factual source.

---

## 📝 MCQ System

The application provides a dedicated MCQ workflow.

```mermaid
flowchart TD
    A["👤 User"] --> B["🔢 Number of Questions"]
    B --> C["🎚️ Difficulty"]
    C --> D["🔗 LangGraph"]
    D --> E["🔎 MMR Retriever"]
    E --> F["📚 Transcript Context"]
    F --> G["🤖 Structured LLM"]
    G --> H["📦 MCQResponse"]
    H --> I["🎯 Interactive Quiz"]
    H --> J["📄 PDF"]
```

Users can select:

```text
Questions: 1–20

Difficulty:
Easy
Medium
Hard
```

---

## 🧩 Structured MCQ Output

Pydantic is used to enforce predictable output:

```python
class MCQ(BaseModel):
    question: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: Literal["A", "B", "C", "D"]
    explanation: str
```

Complete response:

```python
class MCQResponse(BaseModel):
    questions: List[MCQ]
```

Structured output:

```python
llm.with_structured_output(MCQResponse)
```

### MCQ Structure

```text
Question
   ↓
Option A
Option B
Option C
Option D
   ↓
Correct Answer
   ↓
Explanation
```

---

## 🛡️ MCQ Grounding

The MCQ prompt instructs the model to:

- Generate exactly the requested number of questions
- Use only information explicitly present in the transcript
- Never use outside knowledge
- Never invent information
- Generate exactly four options
- Generate exactly one correct answer
- Use A, B, C, and D
- Provide explanations
- Avoid duplicate questions
- Test understanding
- Follow the selected difficulty

---

## 🎯 Interactive Quiz

After MCQs are generated, the user can take an interactive quiz.

```text
A. Option A
B. Option B
C. Option C
D. Option D
```

The user selects an answer using Streamlit radio buttons.

After clicking:

```text
✅ Submit Quiz
```

the application compares the answer with:

```python
mcq.correct_answer
```

### Score

```text
Correct Answers
───────────────
Total Questions
```

Example:

```text
Your Score: 4/5
```

The application then displays the correct answer and explanation for each question.

---

## 📄 PDF Generation

MCQs can be exported using ReportLab.

The utility is:

```python
generate_mcq_pdf()
```

Located at:

```text
backend/utils/pdf_generator.py
```

The PDF is generated in memory using:

```python
BytesIO()
```

### PDF Flow

```text
Generated MCQs
      ↓
generate_mcq_pdf()
      ↓
ReportLab
      ↓
BytesIO
      ↓
PDF Bytes
      ↓
Streamlit Download
```

PDF contains:

```text
MCQ Quiz

Difficulty
Total Questions

Question 1
A. ...
B. ...
C. ...
D. ...

Question 2
A. ...
B. ...
C. ...
D. ...

Answer Key
Explanations
```

---

## 🎨 Streamlit Interface

The application uses Streamlit.

```python
st.set_page_config(
    page_title="YouTube AI",
    page_icon="▶️",
    layout="wide",
    initial_sidebar_state="expanded",
)
```

### UI Layout

```text
┌────────────────────────────────────────────────────────────┐
│                  🎥 YouTube Assistant                      │
├──────────────────────────┬─────────────────────────────────┤
│                          │                                 │
│ 🎬 YouTube URL           │       ▶️ YouTube Video          │
│                          │                                 │
│ [ URL Input ]            │                                 │
│                          │       💬 Chat Messages          │
│ ▶ Load Video             │                                 │
│                          │                                 │
│ ＋ New Chat               │       Chat Composer             │
│                          │                                 │
│ 💬 Chat History          │  ＋ Ask anything...         ↑   │
│                          │                                 │
└──────────────────────────┴─────────────────────────────────┘
```

### Video Player

```python
st.video(
    f"https://www.youtube.com/watch?v={video_id}"
)
```

---

## 🧰 Technology Stack

| Technology | Role |
|---|---|
| 🐍 Python | Application development |
| 🎨 Streamlit | Web application interface |
| 🦜 LangChain | LLM and RAG components |
| 🔗 LangGraph | Stateful workflow orchestration |
| 🤗 Hugging Face | Embedding generation |
| 🧠 BGE Small EN v1.5 | Text embeddings |
| 🔎 FAISS | Vector similarity search |
| ⚡ Groq | LLM inference |
| 🐘 PostgreSQL | Conversation checkpoint storage |
| ▶️ YoutubeLoader | Transcript extraction |
| 📝 Pydantic | Structured MCQ output |
| 📄 ReportLab | PDF generation |
| 🎨 Custom CSS | Streamlit UI styling |

---

## 📁 Project Structure

```text
ai-yt-chatbot/
│
├── app.py
├── styles.py
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
│   │   └── mcq.py
│   │
│   ├── graph/
│   │   ├── graph.py
│   │   └── state.py
│   │
│   ├── database/
│   │   └── postgres.py
│   │
│   ├── assistant/
│   │   └── youtube_assistant.py
│   │
│   └── utils/
│       └── pdf_generator.py
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

> Update this structure if your actual repository uses different filenames or folders.

---

## 🔐 Environment Variables

Create `.env` in the project root:

```env
HF_TOKEN=your_huggingface_token
GROQ_API_KEY=your_groq_api_key
POSTGRES_URL=your_postgresql_connection_string
```

| Variable | Required | Description |
|---|---|---|
| `HF_TOKEN` | ✅ | Hugging Face authentication token |
| `GROQ_API_KEY` | ✅ | Groq API key |
| `POSTGRES_URL` | ✅ | PostgreSQL connection string |

Example:

```env
POSTGRES_URL=postgresql://username:password@localhost:5432/youtube_chat
```

> ⚠️ Never commit `.env` to GitHub.

---

## 🚀 Installation

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-yt-chatbot.git
cd ai-yt-chatbot
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure `.env`

```env
HF_TOKEN=your_huggingface_token
GROQ_API_KEY=your_groq_api_key
POSTGRES_URL=your_postgresql_connection_string
```

### 5. Configure PostgreSQL

Make sure PostgreSQL is running and the database specified in `POSTGRES_URL` exists.

The application initializes:

```python
self.checkpointer = self.database.initialize()
```

and passes it to:

```python
build_graph(
    self.retriever,
    self.model,
    self.checkpointer
)
```

---

## ▶️ Usage

Start the application:

```bash
streamlit run app.py
```

---

### 🎬 Load a Video

Paste:

```text
https://www.youtube.com/watch?v=VIDEO_ID
```

Then click:

```text
▶ Load Video
```

Processing:

```text
YouTube URL
     ↓
Extract Video ID
     ↓
Initialize Embeddings
     ↓
Load / Create FAISS
     ↓
Create Retriever
     ↓
Initialize PostgreSQL
     ↓
Build LangGraph
     ↓
🎥 Video Ready
```

---

### 💬 Ask Questions

Example:

```text
What is the main topic of this video?
```

Processing:

```text
Question
   ↓
Retriever
   ↓
Relevant Transcript
   ↓
LangGraph
   ↓
Groq LLM
   ↓
Grounded Answer
```

---

### 💬 Follow-Up Questions

Example:

```text
👤 What is the main topic?

🤖 The video discusses...

👤 What are the important points?

🤖 The important points are...

👤 Explain the second one.

🤖 The second point refers to...
```

The same `thread_id` maintains conversation state.

---

### 📝 Generate MCQs

Open:

```text
＋ → 📝 Generate MCQs
```

Select:

```text
Number: 1–20
Difficulty: Easy / Medium / Hard
```

Then click:

```text
📝 Generate MCQs
```

---

### 🎯 Take the Quiz

1. Read the question.
2. Select an answer.
3. Click **Submit Quiz**.
4. View your score.
5. Review explanations.

---

### 📄 Download PDF

Click:

```text
📄 Download MCQ Quiz as PDF
```

The generated PDF contains:

- Questions
- Four options
- Difficulty
- Question count
- Answer key
- Explanations

---

## ♻️ FAISS Caching

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

### Future Request

```text
YouTube URL
     ↓
Extract Video ID
     ↓
Check FAISS
     ↓
Index Exists
     ↓
Load Existing Index
```

Indexes:

```text
faiss_indexes/<video_id>/
```

This avoids repeating expensive transcript processing and embedding generation.

---

## 🧩 Core Components

| Component | Responsibility |
|---|---|
| `get_video_id()` | Extracts YouTube video ID |
| `get_embed()` | Initializes embeddings |
| `get_vectorstore()` | Creates or loads FAISS |
| `create_retriever()` | Creates MMR retriever |
| `create_llm()` | Initializes LLM |
| `create_mcq_chain()` | Creates structured MCQ chain |
| `build_graph()` | Creates LangGraph |
| `retrieve_node()` | Retrieves transcript documents |
| `chat_node()` | Generates grounded answers |
| `mcq_node()` | Generates structured MCQs |
| `Database` | Manages PostgreSQL |
| `YouTubeAssistant` | Main application interface |
| `generate_mcq_pdf()` | Generates PDF |
| `create_new_chat()` | Creates chat session |
| `load_chat_video()` | Loads selected video |

---

## 🧠 LangGraph State

```python
class YTChatState(TypedDict, total=False):
    question: str
    context: str
    answer: str
    documents: List[Document]
    messages: Annotated[List[BaseMessage], add_messages]
    mode: str
    number: int
    difficulty: str
    mcqs: object
```

State contains:

```text
Question
Context
Documents
Answer
Messages
Mode
Number
Difficulty
MCQs
```

---

## 🔗 LangGraph Workflow

```mermaid
flowchart TD
    START(["START"])
    RETRIEVE["🔎 Retrieve Node"]
    ROUTER{"⚙️ Mode Router"}
    CHAT["💬 Chat Node"]
    MCQ["📝 MCQ Node"]
    END(["END"])

    START --> RETRIEVE
    RETRIEVE --> ROUTER

    ROUTER -->|chat| CHAT
    ROUTER -->|mcq| MCQ

    CHAT --> END
    MCQ --> END
```

### Retrieve Node

```python
docs = retriever.invoke(query)
```

Flow:

```text
Question
   ↓
Retriever
   ↓
Relevant Documents
   ↓
Context
```

### Router Node

```python
mode = state.get("mode", "chat")
```

If:

```python
mode == "mcq"
```

the graph routes to the MCQ node.

Otherwise, it routes to the chat node.

```text
                 ┌──── chat ────→ 💬 Chat Node
🔎 Retrieve ───→ Router
                 └──── mcq ─────→ 📝 MCQ Node
```

### Chat Node

Uses:

```python
chat_prompt | model | StrOutputParser()
```

Returns:

```python
{
    "answer": response,
    "messages": [AIMessage(content=response)]
}
```

### MCQ Node

Uses:

```python
mcq_chain = create_mcq_chain(model)
```

Structured output:

```python
structured_llm = llm.with_structured_output(MCQResponse)
```

Returns:

```python
{
    "mcqs": result
}
```

---

## 🛡️ Hallucination Control

The chat prompt contains:

```text
Answer ONLY using the provided video transcript context.
```

If the requested information is not present:

```text
The video doesn't mention this
```

### Grounding Flow

```text
👤 User Question
       ↓
🔎 Retriever
       ↓
📚 Relevant Transcript?
       │
       ├── YES ──→ 📖 Context ──→ 🤖 LLM ──→ 💡 Answer
       │
       └── NO ───→ "The video doesn't mention this"
```

> ⚠️ RAG cannot guarantee zero hallucinations. Final response quality depends on transcript quality, retrieval quality, prompt adherence, and model behavior.

---

## 🧪 Example

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

---

## 📝 MCQ Example

```text
User
 ↓
Generate MCQs
 ↓
Select:
 ├── Number: 5
 └── Difficulty: Medium
 ↓
LangGraph
 ↓
Retriever
 ↓
Transcript Context
 ↓
Structured MCQ LLM
 ↓
MCQResponse
 ↓
Interactive Quiz
```

### Quiz Result

```text
👤 User:
Submit Quiz

🤖 YouTube AI:
Your score: 4/5
```

### PDF

```text
Generated MCQs
      ↓
ReportLab
      ↓
PDF
      ↓
Download
```

---

## 🧹 Closing the Assistant

The assistant provides:

```python
assistant.close()
```

which closes the database connection:

```python
self.database.close()
```

---

## ⚠️ Limitations

- YouTube transcripts must be available.
- Transcript retrieval depends on YouTube availability.
- Current language configuration focuses on English and Hindi.
- FAISS indexes are stored locally.
- PostgreSQL is required for persistent LangGraph checkpoints.
- Retrieval quality depends on chunking, embeddings, and query quality.
- MCQ quality depends on transcript and retrieval quality.
- Currently supports one video per chat.
- Chat history is maintained in Streamlit session state.
- Chat history may not persist across Streamlit restarts without additional persistence.
- Generated MCQs are stored in the current Streamlit session.
- Timestamp citations are not currently displayed.
- No user authentication is implemented.
- No multi-user account system is implemented.

---

## 🔮 Future Improvements

- 🌐 FastAPI backend
- 🎨 React / Next.js frontend
- 🔐 User authentication
- 👥 Multi-user support
- 🎬 Multiple videos per conversation
- 🌍 Automatic language detection
- 🗣️ More transcript languages
- ⏱️ Clickable timestamp citations
- 📚 Source citations
- 🔎 Hybrid keyword + semantic retrieval
- 🧠 Reranking models
- ✍️ Query rewriting
- 📝 Advanced quiz types
- 📊 Quiz analytics
- 🏆 Leaderboards
- 🐳 Docker support
- 🧪 Automated tests
- 🚀 GitHub Actions CI/CD
- 📊 RAG evaluation metrics
- 🔭 LangSmith observability
- 📈 Retrieval analytics
- 💾 Persistent user chat history
- ☁️ Cloud vector database
- 📄 Custom PDF templates

---

## 🤝 Contributing

Contributions are welcome!

### 1. Fork

Click **Fork** on GitHub.

### 2. Clone

```bash
git clone https://github.com/YOUR_USERNAME/ai-yt-chatbot.git
cd ai-yt-chatbot
```

### 3. Create Branch

```bash
git checkout -b feature/your-feature
```

### 4. Make Changes

Implement your feature or fix.

### 5. Commit

```bash
git add .
git commit -m "Add your feature"
```

### 6. Push

```bash
git push origin feature/your-feature
```

Open a Pull Request.

---

## 🔒 Security

Recommended `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
faiss_indexes/
```

Never commit:

```text
❌ API keys
❌ Passwords
❌ .env files
❌ PostgreSQL credentials
❌ Private tokens
❌ Sensitive information
```

If a secret is accidentally pushed to GitHub, revoke or rotate it immediately.

Deleting the file afterward does not remove the secret from Git history.

---

## 📄 License

This project is licensed under the **MIT License**.

Add a `LICENSE` file to the repository containing the MIT License text.

---

## 🙏 Acknowledgements

Built using:

- 🦜 LangChain
- 🔗 LangGraph
- 🤗 Hugging Face
- 🔎 FAISS
- ⚡ Groq
- 🐘 PostgreSQL
- 🎨 Streamlit
- 📄 ReportLab

---

## 👨‍💻 Author

### AYUSH GUPTA

Built with:

```text
Python • Streamlit • LangChain • LangGraph • FAISS
Groq • Hugging Face • PostgreSQL • ReportLab
```

If you found this project useful, consider giving the repository a ⭐ on GitHub!

---

<p align="center">
  <strong>🎥 Learn from YouTube. 💬 Chat with your videos. 📝 Test your knowledge.</strong>
</p>

<p align="center">
  <a href="#-ai-youtube-chatbot">⬆️ Back to Top</a>
</p>

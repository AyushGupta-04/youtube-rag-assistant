# 🎥 AI YouTube Chatbot

<p align="center">
  <strong>Chat with YouTube videos and generate AI-powered MCQ quizzes using Retrieval-Augmented Generation (RAG)</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/LangChain-RAG-1C3C3C?style=for-the-badge" alt="LangChain">
  <img src="https://img.shields.io/badge/LangGraph-Workflow-1C3C3C?style=for-the-badge" alt="LangGraph">
  <img src="https://img.shields.io/badge/FAISS-Vector_Search-FF6F00?style=for-the-badge" alt="FAISS">
  <img src="https://img.shields.io/badge/Groq-LLM-F55036?style=for-the-badge" alt="Groq">
  <img src="https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/ReportLab-PDF-B22222?style=for-the-badge" alt="ReportLab">
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
    <td><a href="#-mcq-generation">📝 MCQ Generation</a></td>
  </tr>
  <tr>
    <td>14</td>
    <td><a href="#-mcq-quiz-system">🎯 MCQ Quiz System</a></td>
  </tr>
  <tr>
    <td>15</td>
    <td><a href="#-pdf-generation">📄 PDF Generation</a></td>
  </tr>
  <tr>
    <td>16</td>
    <td><a href="#-streamlit-interface">🎨 Streamlit Interface</a></td>
  </tr>
  <tr>
    <td>17</td>
    <td><a href="#-tech-stack">🧰 Tech Stack</a></td>
  </tr>
  <tr>
    <td>18</td>
    <td><a href="#-project-structure">📁 Project Structure</a></td>
  </tr>
  <tr>
    <td>19</td>
    <td><a href="#-environment-variables">🔐 Environment Variables</a></td>
  </tr>
  <tr>
    <td>20</td>
    <td><a href="#-installation">🚀 Installation</a></td>
  </tr>
  <tr>
    <td>21</td>
    <td><a href="#-usage">▶️ Usage</a></td>
  </tr>
  <tr>
    <td>22</td>
    <td><a href="#-example">🧪 Example</a></td>
  </tr>
  <tr>
    <td>23</td>
    <td><a href="#-hallucination-control">🛡️ Hallucination Control</a></td>
  </tr>
  <tr>
    <td>24</td>
    <td><a href="#-faiss-caching">♻️ FAISS Caching</a></td>
  </tr>
  <tr>
    <td>25</td>
    <td><a href="#-core-components">🧩 Core Components</a></td>
  </tr>
  <tr>
    <td>26</td>
    <td><a href="#-langgraph-state">🧠 LangGraph State</a></td>
  </tr>
  <tr>
    <td>27</td>
    <td><a href="#-langgraph-workflow">🔗 LangGraph Workflow</a></td>
  </tr>
  <tr>
    <td>28</td>
    <td><a href="#-limitations">⚠️ Limitations</a></td>
  </tr>
  <tr>
    <td>29</td>
    <td><a href="#-future-improvements">🔮 Future Improvements</a></td>
  </tr>
  <tr>
    <td>30</td>
    <td><a href="#-contributing">🤝 Contributing</a></td>
  </tr>
  <tr>
    <td>31</td>
    <td><a href="#-security">🔒 Security</a></td>
  </tr>
  <tr>
    <td>32</td>
    <td><a href="#-license">📄 License</a></td>
  </tr>
  <tr>
    <td>33</td>
    <td><a href="#-acknowledgements">🙏 Acknowledgements</a></td>
  </tr>
  <tr>
    <td>34</td>
    <td><a href="#-author">👨‍💻 Author</a></td>
  </tr>
</table>

---

## 📌 Overview

**AI YouTube Chatbot** is a conversational **Retrieval-Augmented Generation (RAG)** application that allows users to ask questions about YouTube videos and generate multiple-choice quizzes using the video's transcript.

The application combines a Streamlit user interface, LangGraph workflow, FAISS vector retrieval, Groq-powered LLM generation, PostgreSQL conversation checkpoints, and ReportLab PDF generation.

Instead of sending the entire transcript directly to an LLM, the application:

- Extracts the YouTube transcript.
- Splits the transcript into smaller chunks.
- Converts chunks into vector embeddings.
- Stores embeddings in FAISS.
- Retrieves the most relevant transcript sections.
- Passes the retrieved context to a Groq-powered LLM.
- Maintains conversation history using LangGraph and PostgreSQL.
- Generates transcript-grounded MCQs with configurable difficulty.
- Allows users to take the generated quiz.
- Calculates the user's score.
- Generates a downloadable PDF containing questions, answers, and explanations.

The result is a complete YouTube learning assistant that supports both conversational video analysis and transcript-grounded quiz generation.

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
| 🔗 LangGraph | Manages retrieval, chat, and MCQ workflows |
| 💬 Conversational Memory | Supports contextual follow-up questions |
| 🐘 PostgreSQL | Persists LangGraph conversation checkpoints |
| 📝 MCQ Generation | Generates transcript-grounded multiple-choice questions |
| 🎚️ Difficulty Selection | Supports Easy, Medium, and Hard difficulty |
| 🔢 Question Control | Allows users to generate 1–20 questions |
| 🎯 Interactive Quiz | Users can select answers and submit the quiz |
| 📊 Score Calculation | Calculates the user's score after submission |
| 💡 Explanations | Displays explanations for every correct answer |
| 📄 PDF Export | Downloads generated quizzes as PDF files |
| 💬 Multiple Chats | Supports multiple independent chat sessions |
| 🎥 Video Per Chat | Each chat can maintain its own YouTube video |
| 🎨 Streamlit UI | Provides an interactive web-based interface |
| 🛡️ Grounded Answers | Instructs the model to answer using transcript context only |

---

## 🏗️ Architecture

The application follows a Retrieval-Augmented Generation architecture with separate paths for conversational chat and MCQ generation.

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

    H --> I{"Select Mode"}

    I -->|Chat| J["🤖 Groq LLM"]
    J --> K["💬 Final Answer"]

    I -->|MCQ| L["📝 MCQ Structured Output"]
    L --> M["🎯 Interactive Quiz"]
    M --> N["📊 Score"]

    L --> O["📄 ReportLab PDF"]

    P[("🐘 PostgreSQL")] <--> H

High-Level Flow
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
LangGraph
      ↓
 ┌───────────────┬────────────────┐
 │               │                │
 ▼               ▼                │
Chat            MCQ               │
 │               │                │
 ▼               ▼                │
Groq LLM       Structured MCQs    │
 │               │                │
 ▼               ▼                │
Answer         Quiz + PDF         │
 └───────────────┴────────────────┘

🔄 RAG Pipeline
🎬 YouTube URL Processing
The application accepts common YouTube URL formats.

Standard YouTube URL

https://www.youtube.com/watch?v=VIDEO_ID

Short YouTube URL

https://youtu.be/VIDEO_ID

The video ID is extracted using the project's:

get_video_id()

utility.

The extracted video ID is also used to identify the video and its associated FAISS index.

📜 Transcript Extraction
The application loads the YouTube transcript through the existing vector-store processing pipeline.

The loader is configured to support:

language=["en", "hi"]

If a transcript cannot be found, the application raises an error instead of continuing with empty data.

Transcript Flow

YouTube URL
     ↓
Video ID
     ↓
YoutubeLoader
     ↓
Transcript Documents

The transcript is then passed into the chunking and embedding pipeline before the conversational or MCQ workflow begins.

✂️ Text Chunking
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

🧠 Embedding Generation
Each transcript chunk is converted into a vector representation using:

BAAI/bge-small-en-v1.5

through the project's embedding configuration.

Embedding Flow

Transcript Chunk
       ↓
Embedding Model
       ↓
Numerical Vector

These vectors allow the system to perform semantic similarity searches.

💾 FAISS Vector Store
The generated embeddings are stored in FAISS.

Each video receives its own local index:

faiss_indexes/
└── VIDEO_ID/
    ├── index.faiss
    └── index.pkl

This provides two important benefits:

Fast similarity search.
Local caching of processed videos.
The YouTubeAssistant.load_video() method initializes the embeddings, loads or creates the FAISS vector store, and creates the retriever.

🔎 MMR Retrieval
The application uses Maximum Marginal Relevance (MMR) retrieval:

vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 5,
        "fetch_k": 20
    }
)

Retrieval Configuration

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

🤖 LLM Generation
After retrieval, the relevant transcript chunks are passed to the LLM.

The project initializes the LLM through:

create_llm()

The current application uses a Groq-powered model configured by the project.

Generation Pipeline

User Question
      ↓
Retriever
      ↓
Relevant Documents
      ↓
Context
      ↓
Chat Prompt
      ↓
Groq LLM
      ↓
Answer

The chat system prompt explicitly instructs the model to use the retrieved transcript context rather than inventing information.

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

The Streamlit application creates a unique UUID for every new chat.

Example:

first_chat_id = str(uuid.uuid4())

Each chat stores:

title
thread_id
video_url
video_id
messages
mcqs
quiz_submitted
score

This allows users to maintain multiple independent conversations.

Example Conversation

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
The transcript remains the factual source.

📝 MCQ Generation
The updated application introduces a dedicated MCQ generation workflow.

Users can open the MCQ interface from the chat composer using:

＋ → 📝 Generate MCQs

The user can configure:

Number of questions.
Difficulty level.
Number of Questions
The application supports:

1 → 20 questions

Difficulty
The supported difficulty levels are:

Easy
Medium
Hard
The YouTubeAssistant.generate_mcqs() method sends the MCQ request through the same LangGraph workflow used by the application.

response = self.graph.invoke(
    {
        "question": "Generate important MCQs from the video.",
        "mode": "mcq",
        "number": number,
        "difficulty": difficulty
    },
    config=config
)

🎯 MCQ Quiz System
🎯 MCQ Structured Output
The application uses Pydantic models to enforce a predictable MCQ structure.

MCQ Model

class MCQ(BaseModel):
    question: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: Literal["A", "B", "C", "D"]
    explanation: str

Each question contains:

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

The complete response is represented by:

class MCQResponse(BaseModel):
    questions: List[MCQ]

The LLM is configured with:

llm.with_structured_output(MCQResponse)

This allows the application to receive structured MCQ data instead of parsing unstructured text.

🛡️ MCQ Grounding
The MCQ prompt contains strict transcript-grounding instructions.

The model is instructed to:

Generate exactly {number} questions.

and:

Use ONLY information explicitly present in the transcript.

It is also instructed to:

Never use outside knowledge.
Never invent information.
Generate exactly four options.
Generate exactly one correct option.
Use A, B, C, and D.
Provide an explanation.
Avoid duplicate questions.
Test understanding of the transcript.
Follow the selected difficulty.
MCQ Generation Flow

User
 ↓
Select Number
 ↓
Select Difficulty
 ↓
LangGraph
 ↓
MMR Retriever
 ↓
Relevant Transcript Context
 ↓
MCQ Prompt
 ↓
Structured LLM Output
 ↓
MCQResponse
 ↓
Interactive Quiz

🎯 MCQ Quiz System
After MCQs are generated, the application displays them as an interactive quiz.

Each question is displayed with four options:

A. Option A
B. Option B
C. Option C
D. Option D

The user selects an answer using Streamlit radio buttons.

Quiz Submission
When the user clicks:

✅ Submit Quiz

the application compares the selected answer with:

mcq.correct_answer

The score is calculated as:

Correct Answers
───────────────
Total Questions

Example

Your score: 4/5

After submission, the application displays:

Answers & Explanations

for every generated question.

📄 PDF Generation
The application provides a PDF download option for generated MCQs.

The PDF is generated using:

generate_mcq_pdf()

from:

backend/utils/pdf_generator.py

The PDF is generated in memory using:

BytesIO()

and returned as bytes.

PDF Contents
The generated PDF contains:

MCQ
Multiple Choice Quiz

Difficulty: Medium
Total Questions: 5

Quiz Questions
    ↓
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

...

Answer Key & Explanations
    ↓
Correct Answer
Explanation

PDF Flow
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
Streamlit Download Button

The user can download the quiz using:

📄 Download MCQ Quiz as PDF

The PDF includes both the questions and the answer key with explanations.

🎨 Streamlit Interface
The updated application uses Streamlit as the frontend.

The application is configured with:

st.set_page_config(
    page_title="YouTube AI",
    page_icon="▶️",
    layout="wide",
    initial_sidebar_state="expanded",
)

Main Interface
The UI contains:

┌─────────────────────────────────────────────────────┐
│                 YouTube Assistant                   │
├──────────────────────┬──────────────────────────────┤
│                      │                              │
│  YouTube URL         │      YouTube Video           │
│                      │                              │
│  ▶ Load Video        │                              │
│                      │      Chat Messages           │
│  ＋ New Chat          │                              │
│                      │                              │
│  Chats               │      Chat Composer           │
│                      │                              │
└──────────────────────┴──────────────────────────────┘

Sidebar
The sidebar provides:

YouTube URL input.
Load Video button.
New Chat button.
Chat history.
Previous chat selection.
Chat Composer
The chat composer contains:

＋    Ask anything about this video...    ↑

The plus menu currently provides:

📝 Generate MCQs

Video Player
Once a video is loaded, the application displays it using:

st.video(
    f"https://www.youtube.com/watch?v={video_id}"
)

🧰 Tech Stack
Technology	Role
🐍 Python	Application development
🎨 Streamlit	Web application interface
🦜 LangChain	LLM and RAG components
🔗 LangGraph	Stateful workflow orchestration
🤗 Hugging Face	Embedding generation
🧠 BGE Small EN v1.5	Text embeddings
🔎 FAISS	Vector similarity search
⚡ Groq	LLM inference
🤖 Groq LLM	Chat and MCQ generation
🐘 PostgreSQL	Conversation checkpoint storage
▶️ YoutubeLoader	Transcript extraction
📝 Pydantic	Structured MCQ output
📄 ReportLab	PDF generation
🎨 Custom CSS	Streamlit UI styling

📁 Project Structure
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

Example
POSTGRES_URL=postgresql://username:password@localhost:5432/youtube_chat

⚠️ Never commit .env to GitHub.

🚀 Installation
1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/ai-yt-chatbot.git
cd ai-yt-chatbot

Replace YOUR_USERNAME with your GitHub username.

2. Create a Virtual Environment
Windows

python -m venv venv
venv\Scripts\activate

Linux / macOS

python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables
Create:

.env

Add:

HF_TOKEN=your_huggingface_token
GROQ_API_KEY=your_groq_api_key
POSTGRES_URL=your_postgresql_connection_string

5. Configure PostgreSQL
Make sure PostgreSQL is running and the database specified in POSTGRES_URL exists.

The application initializes the LangGraph PostgreSQL checkpointer through the database abstraction:

self.checkpointer = self.database.initialize()

The checkpointer is then passed into:

build_graph(
    self.retriever,
    self.model,
    self.checkpointer
)

▶️ Usage
Run the Streamlit Application
Start the application using:

streamlit run app.py

Streamlit will start the local web application.

Load a YouTube Video
Open the application and paste a YouTube URL into the sidebar.

YouTube URL:
https://www.youtube.com/watch?v=VIDEO_ID

Then click:

▶ Load Video

The application will:

YouTube URL
     ↓
Extract Video ID
     ↓
Initialize Embeddings
     ↓
Load/Create FAISS
     ↓
Create Retriever
     ↓
Initialize PostgreSQL Checkpointer
     ↓
Build LangGraph
     ↓
Video Ready

Ask a Question
After loading the video, enter a question into the chat composer:

What is the main topic of this video?

The assistant retrieves relevant transcript chunks and generates a grounded answer.

💬 Follow-up Questions
You can continue asking questions in the same chat.

👤 User:
What is the main topic?

🤖 Assistant:
The video discusses...

👤 User:
What are the important points?

🤖 Assistant:
The important points are...

👤 User:
Explain the second one.

🤖 Assistant:
The second point refers to...

The same thread_id is used to maintain conversation state.

📝 Generate MCQs
To generate a quiz:

＋
 ↓
📝 Generate MCQs

Choose:

Number of questions:
1–20

and:

Difficulty:
Easy / Medium / Hard

Then click:

📝 Generate MCQs

The application retrieves transcript context and generates structured MCQs.

🎯 Take the Quiz
After generation:

Read each question.
Select one of the four options.
Click Submit Quiz.
View your score.
Review correct answers and explanations.
📄 Download the Quiz as PDF
After MCQs are generated, click:

📄 Download MCQ Quiz as PDF

The application generates a PDF containing:

Quiz questions.
Four options per question.
Difficulty.
Total question count.
Answer key.
Explanations.
🧹 Closing the Assistant
The assistant provides a close method:

assistant.close()

This closes the database connection through:

self.database.close()

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

MCQ Mode
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

Quiz Result
👤 User:
Submit Quiz

🤖 YouTube AI:
Your score: 4/5

PDF
Generated MCQs
      ↓
ReportLab
      ↓
PDF
      ↓
Download

🛡️ Hallucination Control
The chat system prompt contains the following core instruction:

Answer ONLY using the provided video transcript context.

If the requested information is not present in the retrieved context, the model is instructed to return:

The video doesn't mention this

Grounding Strategy
👤 User Question
       ↓
🔎 Retriever
       ↓
Relevant Transcript?
       ↓
📚 Provide Context to LLM
       ↓
🤖 Generate Grounded Answer
       ↓
The video doesn't mention this

The MCQ system follows the same grounding principle.

The MCQ prompt explicitly instructs the model:

Use ONLY information explicitly present in the transcript.

It also prohibits:

Outside knowledge.
Invented information.
Unsupported facts.
Note: RAG cannot guarantee zero hallucinations. The final response still depends on transcript quality, retrieval quality, prompt adherence, and model behavior.

♻️ FAISS Caching
The application avoids repeatedly processing the same video.

First Request
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

Subsequent Request
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

The YouTubeAssistant then creates a retriever from the loaded vector store:

self.retriever = create_retriever(vectorstore)

🧩 Core Components
Component	Responsibility
get_video_id()	Extracts the YouTube video ID
get_embed()	Initializes Hugging Face embeddings
get_vectorstore()	Creates or loads FAISS
create_retriever()	Creates the MMR retriever
create_llm()	Initializes the LLM
create_mcq_chain()	Creates the structured MCQ generation chain
build_graph()	Creates the LangGraph workflow
retrieve_node()	Retrieves relevant transcript documents
chat_node()	Generates grounded chat responses
mcq_node()	Generates structured MCQs
Database	Manages PostgreSQL checkpointer
YouTubeAssistant	Main application interface
generate_mcq_pdf()	Generates downloadable MCQ PDFs
create_new_chat()	Creates a new Streamlit chat session
load_chat_video()	Loads the selected chat's video index

🧠 LangGraph State
The chatbot maintains a structured state:

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

This allows the graph to pass:

User questions.
Retrieved context.
Documents.
Generated answers.
Conversation messages.
Workflow mode.
Number of MCQs.
Difficulty.
Generated MCQs.
between workflow nodes.

🔗 LangGraph Workflow
The updated workflow now supports two modes:

chat
mcq

Workflow
["START"]
     ↓
🔎 Retrieve Node
     ↓
Mode?
   ↙   ↘
chat   mcq
 ↓       ↓
💬      📝
Chat    MCQ
Node    Node
 ↓       ↓
["END"]

Retrieve Node
Question
   ↓
Retriever
   ↓
Relevant Documents
   ↓
Context

The retrieve node calls:

docs = retriever.invoke(query)

and creates a context string containing the retrieved transcript content.

Router Node
The workflow checks:

mode = state.get("mode", "chat")

If:

mode == "mcq"

the graph routes to the MCQ node.

Otherwise, it routes to the chat node.

                 ┌── chat ──→ Chat Node
Retrieve → Router
                 └── mcq ──→ MCQ Node

Chat Node
The chat node uses:

chat_prompt | model | StrOutputParser()

It receives:

Context
+
Conversation Messages

and generates the final answer.

The response is stored as:

{
    "answer": response,
    "messages": [AIMessage(content=response)]
}

MCQ Node
The MCQ node uses:

mcq_chain = create_mcq_chain(model)

The chain uses structured output:

structured_llm = llm.with_structured_output(MCQResponse)

The MCQ node receives:

Context
Number
Difficulty

and returns:

{
    "mcqs": result
}

⚠️ Limitations
Current limitations include:

YouTube transcripts must be available.
Transcript retrieval depends on YouTube availability and configuration.
Current language configuration focuses on English and Hindi.
FAISS indexes are stored locally.
PostgreSQL is required for persistent conversation state.
Retrieval quality depends on chunk size, embeddings, and query quality.
The current LangGraph workflow contains retrieval, chat, and MCQ nodes.
MCQ quality depends on transcript quality and retrieved context.
The application currently supports a single video per chat.
Chat history is maintained in Streamlit session state.
Chat history may not persist across Streamlit application restarts unless additional persistence is implemented.
Generated MCQs are stored in the current Streamlit chat session.
PDF generation currently provides questions, answers, and explanations but does not include interactive answer fields.
Timestamp citation data is not currently surfaced in the Streamlit interface.
No user authentication system is currently implemented.
No multi-user account system is currently implemented.
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
📝 More advanced quiz types
📊 Quiz analytics
🏆 Leaderboards
🐳 Docker support
🧪 Automated tests
🚀 GitHub Actions CI/CD
📊 RAG evaluation metrics
🔭 LangSmith observability
📈 Retrieval and answer-quality analytics
💾 Persistent user chat history
☁️ Cloud-based FAISS/vector database
📄 More customizable PDF templates
🤝 Contributing
Contributions are welcome!

1. Fork the Repository
Click the Fork button on GitHub.

2. Clone Your Fork
git clone https://github.com/YOUR_USERNAME/ai-yt-chatbot.git
cd ai-yt-chatbot

3. Create a Feature Branch
git checkout -b feature/your-feature

4. Make Your Changes
Implement your feature or fix.

5. Commit Your Changes
git add .
git commit -m "Add your feature"

6. Push Your Branch
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
Streamlit
ReportLab
👨‍💻 Author
AYUSH GUPTA
Built with:

Python • Streamlit • LangChain • LangGraph • FAISS • Groq • Hugging Face • PostgreSQL • ReportLab

If you found this project useful, consider giving the repository a ⭐ on GitHub!

<p align="center"> <a href="#-ai-youtube-chatbot">⬆️ Back to Top</a> </p>
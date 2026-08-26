<div align="center">

# 🎥 AI YouTube Chatbot

**Chat with YouTube videos, generate MCQ quizzes, and download them as PDFs using AI-powered RAG**

<p>
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/LangChain-RAG-1C3C3C?style=for-the-badge">
  <img src="https://img.shields.io/badge/LangGraph-Workflow-1C3C3C?style=for-the-badge">
  <img src="https://img.shields.io/badge/FAISS-Vector_Search-FF6F00?style=for-the-badge">
  <img src="https://img.shields.io/badge/Groq-LLM-F55036?style=for-the-badge">
  <img src="https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white">
</p>

</div>

---

<div style="border: 1px solid #d0d7de; border-radius: 12px; padding: 28px; background-color: #ffffff;">

<h2>📌 Overview</h2>

<p>
<strong>AI YouTube Chatbot</strong> is a Streamlit-based conversational RAG application that allows users to interact with YouTube videos using their transcripts.
</p>

<p>
Users can load a YouTube video, ask questions about its content, maintain multiple conversations, generate MCQ quizzes, submit quizzes, view scores and explanations, and download generated quizzes as PDF files.
</p>

<p>The application uses:</p>

<ul>
<li>YouTube transcripts as the knowledge source</li>
<li>FAISS for semantic vector search</li>
<li>MMR retrieval for diverse relevant context</li>
<li>LangGraph for workflow orchestration</li>
<li>Groq for LLM inference</li>
<li>Hugging Face embeddings for semantic search</li>
<li>PostgreSQL for persistent conversation checkpoints</li>
<li>Streamlit for the user interface</li>
<li>ReportLab for MCQ PDF generation</li>
</ul>

<hr>

<h2>✨ Features</h2>

<table>
<tr>
<th>Feature</th>
<th>Description</th>
</tr>
<tr>
<td>🎬 YouTube Integration</td>
<td>Load transcripts directly from YouTube URLs.</td>
</tr>
<tr>
<td>🌐 Multi-language</td>
<td>Supports English and Hindi transcript retrieval.</td>
</tr>
<tr>
<td>✂️ Smart Chunking</td>
<td>Splits transcripts into smaller retrieval-friendly chunks.</td>
</tr>
<tr>
<td>🧠 Embeddings</td>
<td>Uses <code>BAAI/bge-small-en-v1.5</code> for embeddings.</td>
</tr>
<tr>
<td>🔎 Semantic Search</td>
<td>Retrieves transcript sections relevant to user questions.</td>
</tr>
<tr>
<td>🔀 MMR Retrieval</td>
<td>Improves retrieval diversity and reduces redundant results.</td>
</tr>
<tr>
<td>💾 FAISS</td>
<td>Stores transcript embeddings locally.</td>
</tr>
<tr>
<td>♻️ FAISS Caching</td>
<td>Reuses an existing index when the same video is loaded again.</td>
</tr>
<tr>
<td>🤖 Groq LLM</td>
<td>Generates answers using the retrieved transcript context.</td>
</tr>
<tr>
<td>🔗 LangGraph</td>
<td>Manages retrieval, chat, and MCQ generation workflows.</td>
</tr>
<tr>
<td>💬 Multiple Chats</td>
<td>Allows users to create and switch between different conversations.</td>
</tr>
<tr>
<td>📝 MCQ Generation</td>
<td>Generates transcript-grounded multiple-choice questions.</td>
</tr>
<tr>
<td>🎯 Difficulty Selection</td>
<td>Supports Easy, Medium, and Hard quiz difficulty.</td>
</tr>
<tr>
<td>📊 Quiz Evaluation</td>
<td>Calculates the user's score and displays correct answers.</td>
</tr>
<tr>
<td>📄 PDF Export</td>
<td>Downloads generated MCQ quizzes as PDF files.</td>
</tr>
<tr>
<td>🛡️ Grounded Answers</td>
<td>Instructs the LLM to answer using transcript context only.</td>
</tr>
</table>

<hr>

<h2>🏗️ Architecture</h2>

<pre>
                    ┌─────────────────────┐
                    │    YouTube URL      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Extract Video ID   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ YouTube Transcript  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Text Chunking    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Embeddings      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   FAISS Vector DB   │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
                    ▼                     ▼
             ┌──────────────┐      ┌──────────────┐
             │ User Question│      │ MCQ Request  │
             └──────┬───────┘      └──────┬───────┘
                    │                     │
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │    MMR Retriever    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Relevant Context  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      LangGraph      │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
                    ▼                     ▼
             ┌──────────────┐      ┌──────────────┐
             │   Chat Node  │      │   MCQ Node   │
             └──────┬───────┘      └──────┬───────┘
                    │                     │
                    ▼                     ▼
             ┌──────────────┐      ┌──────────────┐
             │   Groq LLM   │      │ MCQResponse  │
             └──────┬───────┘      └──────┬───────┘
                    │                     │
                    ▼                     ▼
             ┌──────────────┐      ┌──────────────┐
             │ Final Answer │      │ Quiz + PDF   │
             └──────────────┘      └──────────────┘

                     PostgreSQL
                         │
                         ▼
                  Conversation
                   Checkpoints
</pre>

<hr>

<h2>🔄 RAG Pipeline</h2>

<pre>
YouTube URL
     ↓
Video ID
     ↓
Transcript
     ↓
Text Chunks
     ↓
Hugging Face Embeddings
     ↓
FAISS
     ↓
MMR Retrieval
     ↓
Relevant Transcript Context
     ↓
LangGraph
     ↓
Groq LLM
     ↓
Final Answer
</pre>

<p>
The application does not send the complete transcript to the LLM. Instead, it retrieves the most relevant transcript chunks and provides those chunks as context.
</p>

<hr>

<h2>🎬 YouTube URL Processing</h2>

<p>The application accepts common YouTube URL formats.</p>

<pre>
https://www.youtube.com/watch?v=VIDEO_ID

https://youtu.be/VIDEO_ID
</pre>

<p>
The video ID is extracted using the project's <code>get_video_id()</code> utility.
The video ID is also used to identify the corresponding FAISS index.
</p>

<hr>

<h2>📜 Transcript Extraction</h2>

<p>
The application loads the YouTube transcript through the project's YouTube loader.
The transcript configuration supports:
</p>

<pre>
language=["en", "hi"]
</pre>

<p>The transcript is then passed to the chunking stage.</p>

<pre>
YouTube URL
     ↓
Video ID
     ↓
Transcript Loader
     ↓
Transcript Documents
</pre>

<hr>

<h2>✂️ Text Chunking</h2>

<p>
Transcript documents are divided into smaller chunks before embeddings are generated.
</p>

<pre>
RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)
</pre>

<table>
<tr>
<th>Parameter</th>
<th>Value</th>
</tr>
<tr>
<td>Chunk Size</td>
<td><code>800</code></td>
</tr>
<tr>
<td>Chunk Overlap</td>
<td><code>150</code></td>
</tr>
</table>

<p>
The overlap helps preserve context between neighboring transcript chunks.
</p>

<hr>

<h2>🧠 Embedding Generation</h2>

<p>
Each transcript chunk is converted into a numerical vector using:
</p>

<pre>
BAAI/bge-small-en-v1.5
</pre>

<p>
The project initializes the embedding model through the <code>get_embed()</code> function.
These vectors are used for semantic similarity search.
</p>

<pre>
Transcript Chunk
       ↓
Embedding Model
       ↓
Vector Representation
       ↓
FAISS
</pre>

<hr>

<h2>💾 FAISS Vector Store</h2>

<p>
FAISS is used as the local vector store for transcript embeddings.
Each YouTube video gets its own cached index.
</p>

<pre>
faiss_indexes/
└── VIDEO_ID/
    ├── index.faiss
    └── index.pkl
</pre>

<p>This provides:</p>

<ul>
<li>Fast similarity search</li>
<li>Local vector storage</li>
<li>Reuse of previously processed videos</li>
<li>Reduced repeated embedding generation</li>
</ul>

<hr>

<h2>🔎 MMR Retrieval</h2>

<p>
The application uses Maximum Marginal Relevance retrieval.
</p>

<pre>
vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 5,
        "fetch_k": 20
    }
)
</pre>

<table>
<tr>
<th>Parameter</th>
<th>Value</th>
<th>Purpose</th>
</tr>
<tr>
<td>search_type</td>
<td><code>mmr</code></td>
<td>Uses Maximum Marginal Relevance</td>
</tr>
<tr>
<td>k</td>
<td><code>5</code></td>
<td>Final documents returned</td>
</tr>
<tr>
<td>fetch_k</td>
<td><code>20</code></td>
<td>Candidate documents considered</td>
</tr>
</table>

<p>
MMR attempts to provide relevant and diverse transcript chunks instead of returning several nearly identical chunks.
</p>

<hr>

<h2>🤖 LLM Generation</h2>

<p>The application uses Groq for LLM inference.</p>

<pre>
ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.3
)
</pre>

<p>The chat generation flow is:</p>

<pre>
User Question
      ↓
MMR Retriever
      ↓
Relevant Documents
      ↓
Transcript Context
      ↓
Chat Prompt
      ↓
Groq LLM
      ↓
Answer
</pre>

<hr>

<h2>💬 Conversation Memory</h2>

<p>
Conversation state is maintained using LangGraph with PostgreSQL checkpoints.
Every chat has its own unique <code>thread_id</code>.
</p>

<pre>
thread_id = UUID
</pre>

<p>Example:</p>

<pre>
{
    "configurable": {
        "thread_id": "conversation-1"
    }
}
</pre>

<p>
This allows the chatbot to maintain context across follow-up questions.
</p>

<pre>
User:
What is the main topic?

Assistant:
The video discusses artificial intelligence.

User:
What are the three main points?

Assistant:
The three main points are...

User:
Explain the second one.

Assistant:
The second point refers to...
</pre>

<hr>

<h2>💬 Multiple Chat Support</h2>

<p>
The Streamlit application supports multiple independent conversations.
Each chat contains:
</p>

<ul>
<li>Unique chat ID</li>
<li>Unique thread ID</li>
<li>Chat title</li>
<li>YouTube URL</li>
<li>YouTube video ID</li>
<li>Chat messages</li>
<li>Generated MCQs</li>
<li>Quiz score</li>
<li>Quiz submission state</li>
</ul>

<p>Each new chat is created using a UUID:</p>

<pre>
chat_id = str(uuid.uuid4())
</pre>

<p>
Users can switch between chats from the sidebar.
When an old chat is selected, its associated video's FAISS index is loaded again.
</p>

<hr>

<h2>📝 MCQ Generation</h2>

<p>
The application includes a dedicated MCQ generation mode.
Users can choose:
</p>

<ul>
<li>Number of questions: 1–20</li>
<li>Difficulty: Easy, Medium, Hard</li>
</ul>

<p>The MCQ generation flow is:</p>

<pre>
YouTube Transcript
       ↓
MMR Retrieval
       ↓
Relevant Context
       ↓
MCQ Prompt
       ↓
Structured LLM Output
       ↓
MCQResponse
       ↓
Quiz
</pre>

<p>
The MCQs are generated using structured Pydantic output.
</p>

<hr>

<h2>🎯 MCQ Structure</h2>

<pre>
MCQ
├── question
├── option_a
├── option_b
├── option_c
├── option_d
├── correct_answer
└── explanation
</pre>

<p>The correct answer is restricted to:</p>

<pre>
A
B
C
D
</pre>

<p>
The application instructs the model to generate exactly the requested number of questions and use only information available in the transcript.
</p>

<hr>

<h2>📊 Quiz Evaluation</h2>

<p>
After MCQs are generated, users can select an answer for every question and submit the quiz.
</p>

<pre>
Selected Answers
       ↓
Compare with correct_answer
       ↓
Calculate Score
       ↓
Display Result
</pre>

<p>Example:</p>

<pre>
Your score: 4/5
</pre>

<p>
After submission, the application also displays the correct answer and explanation for every question.
</p>

<hr>

<h2>📄 MCQ PDF Generation</h2>

<p>
Generated quizzes can be downloaded as PDF files using ReportLab.
</p>

<pre>
Generated MCQs
      ↓
generate_mcq_pdf()
      ↓
ReportLab
      ↓
PDF Bytes
      ↓
Streamlit Download
</pre>

<p>The generated PDF contains:</p>

<ul>
<li>Quiz title</li>
<li>Difficulty</li>
<li>Total number of questions</li>
<li>All MCQ questions</li>
<li>Four options for each question</li>
<li>Answer key</li>
<li>Explanations</li>
</ul>

<p>The PDF is generated in memory using <code>BytesIO</code>, so no temporary PDF file is required.</p>

<hr>

<h2>🛡️ Hallucination Control</h2>

<p>The chat system prompt instructs the model:</p>

<pre>
Answer ONLY using the provided video transcript context.
</pre>

<p>
If the requested information is not available in the retrieved context, the model is instructed to respond:
</p>

<pre>
The video doesn't mention this
</pre>

<p>
The MCQ generator also follows transcript-only generation rules.
It is instructed not to use outside knowledge or invent information.
</p>

<p>
<strong>Important:</strong> RAG does not guarantee zero hallucinations. Final answer quality depends on transcript quality, retrieval quality, prompt adherence, and model behavior.
</p>

<hr>

<h2>♻️ FAISS Caching</h2>

<p>
The application checks for an existing FAISS index before processing the video again.
</p>

<h3>First Load</h3>

<pre>
YouTube URL
     ↓
Video ID
     ↓
Load Transcript
     ↓
Chunk Transcript
     ↓
Generate Embeddings
     ↓
Create FAISS
     ↓
Save Index
</pre>

<h3>Next Load</h3>

<pre>
YouTube URL
     ↓
Video ID
     ↓
Check FAISS
     ↓
Existing Index
     ↓
Load Index
</pre>

<p>
This reduces unnecessary transcript processing and embedding generation when a video has already been processed.
</p>

<hr>

<h2>🧠 LangGraph Workflow</h2>

<pre>
                    START
                      │
                      ▼
               ┌─────────────┐
               │   Retrieve  │
               └──────┬──────┘
                      │
                Check Mode
                 /        \
                /          \
               ▼            ▼
        ┌──────────┐   ┌──────────┐
        │   Chat   │   │   MCQ    │
        └────┬─────┘   └────┬─────┘
             │              │
             ▼              ▼
            END            END
</pre>

<h3>Retrieve Node</h3>

<p>
The retrieve node receives the question and searches the FAISS retriever.
The retrieved documents are converted into a context string.
</p>

<pre>
Question
   ↓
Retriever
   ↓
Documents
   ↓
Context
</pre>

<h3>Chat Node</h3>

<pre>
Context
   +
Conversation Messages
   +
Question
   ↓
Chat Prompt
   ↓
Groq LLM
   ↓
Answer
</pre>

<h3>MCQ Node</h3>

<pre>
Context
   +
Number
   +
Difficulty
   ↓
MCQ Prompt
   ↓
Structured LLM
   ↓
MCQResponse
</pre>

<hr>

<h2>🧩 Core Components</h2>

<table>
<tr>
<th>Component</th>
<th>Responsibility</th>
</tr>
<tr>
<td><code>get_video_id()</code></td>
<td>Extracts the YouTube video ID.</td>
</tr>
<tr>
<td><code>get_embed()</code></td>
<td>Initializes the embedding model.</td>
</tr>
<tr>
<td><code>get_vectorstore()</code></td>
<td>Creates or loads the FAISS vector store.</td>
</tr>
<tr>
<td><code>create_retriever()</code></td>
<td>Creates the MMR retriever.</td>
</tr>
<tr>
<td><code>create_llm()</code></td>
<td>Initializes the Groq LLM.</td>
</tr>
<tr>
<td><code>build_graph()</code></td>
<td>Builds the LangGraph workflow.</td>
</tr>
<tr>
<td><code>create_mcq_chain()</code></td>
<td>Creates the structured MCQ generation chain.</td>
</tr>
<tr>
<td><code>generate_mcq_pdf()</code></td>
<td>Creates the downloadable MCQ PDF.</td>
</tr>
<tr>
<td><code>YouTubeAssistant</code></td>
<td>Main interface for video loading, chat, and MCQ generation.</td>
</tr>
<tr>
<td><code>Database</code></td>
<td>Manages PostgreSQL conversation checkpoints.</td>
</tr>
</table>

<hr>

<h2>🧠 LangGraph State</h2>

<pre>
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
</pre>

<p>The state contains:</p>

<ul>
<li>User question</li>
<li>Retrieved context</li>
<li>Generated answer</li>
<li>Retrieved documents</li>
<li>Conversation messages</li>
<li>Current mode</li>
<li>Number of MCQs</li>
<li>Difficulty</li>
<li>Generated MCQs</li>
</ul>

<hr>

<h2>🧰 Tech Stack</h2>

<table>
<tr>
<th>Technology</th>
<th>Role</th>
</tr>
<tr>
<td>🐍 Python</td>
<td>Application development</td>
</tr>
<tr>
<td>🎨 Streamlit</td>
<td>User interface</td>
</tr>
<tr>
<td>🦜 LangChain</td>
<td>LLM and RAG components</td>
</tr>
<tr>
<td>🔗 LangGraph</td>
<td>Workflow orchestration</td>
</tr>
<tr>
<td>🤗 Hugging Face</td>
<td>Embedding generation</td>
</tr>
<tr>
<td>🧠 BGE Small EN v1.5</td>
<td>Text embeddings</td>
</tr>
<tr>
<td>🔎 FAISS</td>
<td>Vector similarity search</td>
</tr>
<tr>
<td>⚡ Groq</td>
<td>LLM inference</td>
</tr>
<tr>
<td>🤖 GPT-OSS-20B</td>
<td>Language model</td>
</tr>
<tr>
<td>🐘 PostgreSQL</td>
<td>Conversation checkpoint storage</td>
</tr>
<tr>
<td>📄 ReportLab</td>
<td>PDF generation</td>
</tr>
</table>

<hr>

<h2>📁 Project Structure</h2>

<pre>
ai-yt-chatbot/
│
├── backend/
│   │
│   ├── assistant/
│   │   └── youtube_assistant.py
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
│   └── utils/
│       └── pdf_generator.py
│
├── faiss_indexes/
│   └── &lt;video_id&gt;/
│       ├── index.faiss
│       └── index.pkl
│
├── app.py
├── styles.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
</pre>

<hr>

<h2>🔐 Environment Variables</h2>

<p>Create a <code>.env</code> file in the project root.</p>

<pre>
HF_TOKEN=your_huggingface_token
GROQ_API_KEY=your_groq_api_key
POSTGRES_URL=your_postgresql_connection_string
</pre>

<table>
<tr>
<th>Variable</th>
<th>Required</th>
<th>Description</th>
</tr>
<tr>
<td><code>HF_TOKEN</code></td>
<td>✅</td>
<td>Hugging Face authentication token.</td>
</tr>
<tr>
<td><code>GROQ_API_KEY</code></td>
<td>✅</td>
<td>Groq API key.</td>
</tr>
<tr>
<td><code>POSTGRES_URL</code></td>
<td>✅</td>
<td>PostgreSQL connection string.</td>
</tr>
</table>

<p>Example:</p>

<pre>
POSTGRES_URL=postgresql://username:password@localhost:5432/youtube_chat
</pre>

<p>⚠️ Never commit your <code>.env</code> file to GitHub.</p>

<hr>

<h2>🚀 Installation</h2>

<h3>1. Clone the Repository</h3>

<pre>
git clone https://github.com/YOUR_USERNAME/ai-yt-chatbot.git
cd ai-yt-chatbot
</pre>

<h3>2. Create a Virtual Environment</h3>

<p><strong>Windows:</strong></p>

<pre>
python -m venv venv
venv\Scripts\activate
</pre>

<p><strong>Linux / macOS:</strong></p>

<pre>
python3 -m venv venv
source venv/bin/activate
</pre>

<h3>3. Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<h3>4. Configure Environment Variables</h3>

<pre>
HF_TOKEN=your_huggingface_token
GROQ_API_KEY=your_groq_api_key
POSTGRES_URL=your_postgresql_connection_string
</pre>

<h3>5. Configure PostgreSQL</h3>

<p>
Make sure PostgreSQL is running and the database specified in <code>POSTGRES_URL</code> exists.
</p>

<hr>

<h2>▶️ Usage</h2>

<h3>Start the Application</h3>

<pre>
streamlit run app.py
</pre>

<p>
The Streamlit application will open in your browser.
</p>

<h3>Load a Video</h3>

<ol>
<li>Paste a YouTube URL into the sidebar.</li>
<li>Click <strong>Load Video</strong>.</li>
<li>Wait for the transcript and FAISS index to load.</li>
<li>Start asking questions.</li>
</ol>

<h3>Ask Questions</h3>

<pre>
What is the main topic of this video?
</pre>

<h3>Generate MCQs</h3>

<ol>
<li>Click the <strong>＋</strong> button beside the chat input.</li>
<li>Select <strong>Generate MCQs</strong>.</li>
<li>Select the number of questions.</li>
<li>Select the difficulty.</li>
<li>Click <strong>Generate MCQs</strong>.</li>
</ol>

<h3>Download Quiz</h3>

<p>
After generating the quiz, click:
</p>

<pre>
📄 Download MCQ Quiz as PDF
</pre>

<h3>Submit Quiz</h3>

<p>
Select answers and click:
</p>

<pre>
✅ Submit Quiz
</pre>

<p>
The application displays your score along with the correct answers and explanations.
</p>

<hr>

<h2>🧪 Example</h2>

<h3>Step 1 — Load Video</h3>

<pre>
https://www.youtube.com/watch?v=VIDEO_ID
</pre>

<h3>Step 2 — Ask a Question</h3>

<pre>
What are the main points discussed in this video?
</pre>

<h3>Step 3 — Chatbot Processing</h3>

<pre>
Question
   ↓
MMR Retrieval
   ↓
Relevant Transcript Chunks
   ↓
LangGraph
   ↓
Groq LLM
   ↓
Answer
</pre>

<h3>Step 4 — Generate Quiz</h3>

<pre>
Transcript Context
      ↓
MCQ Chain
      ↓
Structured MCQResponse
      ↓
Quiz
</pre>

<h3>Step 5 — Download PDF</h3>

<pre>
Quiz
 ↓
ReportLab
 ↓
PDF
 ↓
Download
</pre>

<hr>

<h2>⚠️ Limitations</h2>

<ul>
<li>YouTube transcripts must be available.</li>
<li>Transcript retrieval depends on YouTube availability.</li>
<li>Current transcript language configuration focuses on English and Hindi.</li>
<li>FAISS indexes are stored locally.</li>
<li>PostgreSQL is required for persistent conversation checkpoints.</li>
<li>Retrieval quality depends on chunking, embeddings, and query quality.</li>
<li>LLM responses may still contain occasional hallucinations.</li>
<li>Multiple chats currently share the same assistant instance.</li>
<li>Only one YouTube video is associated with each chat.</li>
<li>There is currently no authentication system.</li>
</ul>

<hr>

<h2>🔮 Future Improvements</h2>

<ul>
<li>🌐 FastAPI backend</li>
<li>🎨 Improved frontend</li>
<li>🔐 User authentication</li>
<li>👥 Multi-user support</li>
<li>🎬 Multiple videos per conversation</li>
<li>🌍 Automatic language detection</li>
<li>🗣️ More transcript languages</li>
<li>⏱️ Clickable timestamp citations</li>
<li>📚 Source citations in answers</li>
<li>🔎 Hybrid keyword + semantic retrieval</li>
<li>🧠 Reranking models</li>
<li>✍️ Query rewriting</li>
<li>🐳 Docker support</li>
<li>🧪 Automated tests</li>
<li>🚀 GitHub Actions CI/CD</li>
<li>📊 RAG evaluation metrics</li>
<li>🔭 LangSmith observability</li>
</ul>

<hr>

<h2>🤝 Contributing</h2>

<p>Contributions are welcome!</p>

<h3>1. Fork the Repository</h3>

<p>Click the <strong>Fork</strong> button on GitHub.</p>

<h3>2. Clone Your Fork</h3>

<pre>
git clone https://github.com/YOUR_USERNAME/ai-yt-chatbot.git
cd ai-yt-chatbot
</pre>

<h3>3. Create a Feature Branch</h3>

<pre>
git checkout -b feature/your-feature
</pre>

<h3>4. Make Your Changes</h3>

<p>Implement your feature or fix.</p>

<h3>5. Commit Your Changes</h3>

<pre>
git add .
git commit -m "Add your feature"
</pre>

<h3>6. Push Your Branch</h3>

<pre>
git push origin feature/your-feature
</pre>

<p>Then open a Pull Request on GitHub.</p>

<hr>

<h2>🔒 Security</h2>

<p>Make sure your <code>.gitignore</code> contains:</p>

<pre>
.env
venv/
__pycache__/
*.pyc
faiss_indexes/
</pre>

<p>Never commit:</p>

<ul>
<li>❌ API keys</li>
<li>❌ Passwords</li>
<li>❌ <code>.env</code> files</li>
<li>❌ PostgreSQL credentials</li>
<li>❌ Private tokens</li>
<li>❌ Sensitive information</li>
</ul>

<p>
If a secret is accidentally pushed to GitHub, revoke or rotate it immediately.
Deleting the file afterward does not remove the secret from Git history.
</p>

<hr>

<h2>📄 License</h2>

<p>
This project is licensed under the <strong>MIT License</strong>.
</p>

<p>
Add a <code>LICENSE</code> file to the root of the repository containing the MIT License text.
</p>

<hr>

<h2>🙏 Acknowledgements</h2>

<ul>
<li>LangChain</li>
<li>LangGraph</li>
<li>Hugging Face</li>
<li>FAISS</li>
<li>Groq</li>
<li>PostgreSQL</li>
<li>Streamlit</li>
<li>ReportLab</li>
<li>YouTube</li>
</ul>

<hr>

<h2>👨‍💻 Author</h2>

<h3>AYUSH GUPTA</h3>

<p>
Built with:
</p>

<p>
<strong>Python • Streamlit • LangChain • LangGraph • FAISS • Groq • Hugging Face • PostgreSQL • ReportLab</strong>
</p>

<p>
If you found this project useful, consider giving the repository a ⭐ on GitHub!
</p>

<hr>

<div align="center">

<h3>⬆️ Back to Top</h3>

<p>
<strong>AI YouTube Chatbot</strong> — Chat • Learn • Quiz • Download
</p>

</div>

</div>

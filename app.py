import uuid
import streamlit as st
from backend.assistant.youtube_assistant import YouTubeAssistant
from backend.utils.pdf_generator import generate_mcq_pdf
from styles import load_css

# PAGE CONFIG
st.set_page_config(
    page_title="YouTube AI",
    page_icon="▶️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CSS
load_css()

# SESSION STATE
if "assistant" not in st.session_state:
    st.session_state.assistant = YouTubeAssistant()

if "chats" not in st.session_state:
    first_chat_id = str(uuid.uuid4())
    st.session_state.chats = {
        first_chat_id: {
            "title": "New Chat",
            "thread_id": first_chat_id,
            "video_url": None,
            "video_id": None,
            "messages": [],
            "mcqs": None,
            "quiz_submitted": False,
            "score": None,
            "input_version": 0,
        }
    }

    st.session_state.current_chat = first_chat_id

if "mode" not in st.session_state:
    st.session_state.mode = "chat"

# HELPER FUNCTIONS
def create_new_chat():
    chat_id = str(uuid.uuid4())
    st.session_state.chats[chat_id] = {
        "title": "New Chat",
        "thread_id": chat_id,
        "video_url": None,
        "video_id": None,
        "messages": [],
        "mcqs": None,
        "quiz_submitted": False,
        "score": None,
        "input_version": 0,
    }

    st.session_state.current_chat = chat_id
    st.session_state.mode = "chat"

def get_current_chat():
    return st.session_state.chats[st.session_state.current_chat]

def load_chat_video(chat):
    if not chat["video_url"]:
        return None

    return st.session_state.assistant.load_video(chat["video_url"])

# CURRENT CHAT
chat = get_current_chat()

# SIDEBAR
with st.sidebar:
    st.markdown("## ▶️ YouTube AI")
    st.markdown("### YouTube Video")

    # URL INPUT
    url = st.text_input(
        "YouTube URL",
        value=chat["video_url"] or "",
        placeholder="Paste YouTube URL here...",
        label_visibility="collapsed"
    )

    # LOAD VIDEO

    if st.button(
        "▶  Load Video",
        type="primary",
        use_container_width=True
    ):
        if not url.strip():
            st.error("Please enter a YouTube URL.")
        else:
            try:
                with st.spinner("Loading video..."):
                    video_id =  st.session_state.assistant.load_video(url)
                    
                chat["video_url"] = url
                chat["video_id"] = video_id

                # Reset quiz
                chat["mcqs"] = None
                chat["quiz_submitted"] = False
                chat["score"] = None

                # Always start in chat mode
                st.session_state.mode = "chat"
                st.success("Video loaded successfully!")
                st.rerun()


            except Exception as e:
                st.error("Failed to load video.")
                st.exception(e)

    # NEW CHAT
    if st.button("＋  New Chat",use_container_width=True,):
        create_new_chat()
        st.rerun()

    st.divider()

    # CHAT HISTORY
    st.markdown("### Chats")
    chat_items = list(st.session_state.chats.items())
    chat_items.reverse()

    for cid, item in chat_items:
        title = item["title"]

        if not title.strip():
            title = "New Chat"

        if len(title) > 32:
            title = title[:32] + "..."

        if cid == st.session_state.current_chat:
            button_text = "●  " + title

        else:
            button_text = "   " + title

        if st.button(
            button_text,
            key=f"chat_{cid}",
            use_container_width=True
        ):

            st.session_state.current_chat = cid
            selected_chat = st.session_state.chats[cid]
            
            # Load video index
            if selected_chat["video_url"]:
                try:
                    with st.spinner("Loading video's index..."):
                    # Load selected video's index
                        load_chat_video(selected_chat)

                except Exception as e:
                    st.error("Could not load this video's index.")
                    st.exception(e)

            st.session_state.mode = "chat"
            st.rerun()

# MAIN HEADER
st.markdown(
    """
    <div class="main-title">
        YouTube Assistant
    </div>
    """,
    unsafe_allow_html=True,
)

# VIDEO
if chat["video_url"]:
    video_id = chat["video_id"]
    youtube_container = st.container(key="youtube_video")

    with youtube_container:
        st.video(f"https://www.youtube.com/watch?v={video_id}")

else:
    st.info(
        "👈 Paste a YouTube URL in the sidebar "
        "and click **Load Video** to start."
    )

# CHAT HISTORY
for message in chat["messages"]:
    role = message["role"]
    content = message["content"]
    with st.chat_message(role):
        st.markdown(content)

# CHAT MODE
if chat["video_url"] and st.session_state.mode == "chat":
    # SINGLE CHAT COMPOSER
    composer = st.container(key="chat_composer")
    with composer:
        # THREE PARTS
        plus_col, input_col, send_col = st.columns(
            [0.07, 0.83, 0.10],
            gap="small",
            vertical_alignment="center"
        )
        # PLUS
        with plus_col:
            plus_menu = st.popover(
                "＋",
                type="tertiary",
                help="More options",
                key=f"plus_{chat['thread_id']}",
            )

            with plus_menu:
                # ONLY MCQ OPTION
                if st.button(
                    "📝  Generate MCQs",
                    key=f"menu_mcq_{chat['thread_id']}",
                    use_container_width=True
                ):
           
                    # SWITCH TO MCQ MODE
                    st.session_state.mode = "mcq"
                    st.rerun()

        # TEXT INPUT
        with input_col:
            question = st.text_input(
                "Message",
                placeholder="Ask anything about this video...",
                label_visibility="collapsed",
                key=f"question_{chat['thread_id']}_{chat['input_version']}"
            )

        # SEND
        with send_col:
            submitted = st.button(
                "↑",
                key=f"send_{chat['thread_id']}",
                use_container_width=True
            )

    # PROCESS CHAT MESSAGE
    if submitted:
        if not question.strip():
            st.warning("Please enter a question.")

        else:
            question = question.strip()
            # USER MESSAGE
            chat["messages"].append(
                {
                    "role": "user",
                    "content": question
                }
            )

            # CHAT TITLE
            if chat["title"] == "New Chat":
                chat["title"] = question[:40]

            # AI
            try:
                with st.spinner("Thinking..."):
                    answer = st.session_state.assistant.ask(
                        question=question, 
                        thread_id=chat["thread_id"])
                    
                # ASSISTANT MESSAGE
                chat["messages"].append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )
                
                # CREATE A FRESH INPUT WIDGET
                chat["input_version"] += 1
                st.rerun()

            except Exception as e:
                st.error("Something went wrong.")
                st.exception(e)

# MCQ MODE
elif chat["video_url"] and st.session_state.mode == "mcq":
    st.divider()

    # MCQ HEADER

    st.markdown(
        """
        <div class="mcq-title">
            📝 Generate MCQs
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("Create multiple-choice questions using only the YouTube transcript.")

    # BACK TO CHAT

    if st.button("← Back to Chat", key=f"back_chat_{chat['thread_id']}"):
        st.session_state.mode = "chat"
        st.rerun()

    st.divider()

    # SETTINGS
    col1, col2 = st.columns(2)
    with col1:
        number = st.slider(
            "Number of questions",
            min_value=1,
            max_value=20,
            value=5,
            step=1,
            key=f"mcq_number_{chat['thread_id']}"
        )

    with col2:
        difficulty = st.selectbox(
            "Difficulty",
            [
                "Easy",
                "Medium",
                "Hard"
            ],
            index=1,
            key=f"difficulty_{chat['thread_id']}"
        )

    # GENERATE MCQS

    if st.button(
        "📝 Generate MCQs",
        type="primary",
        use_container_width=True,
        key=f"generate_mcq_{chat['thread_id']}"
    ):

        try:
            with st.spinner("Generating MCQs..."):
                result = (
                    st.session_state
                    .assistant
                    .generate_mcqs(
                        number=number,
                        difficulty=difficulty,
                        thread_id=chat["thread_id"],
                    )
                )

            chat["mcqs"] = result.questions
            chat["quiz_submitted"] = False
            chat["score"] = None

            st.success(f"{len(chat['mcqs'])} questions generated!")
            st.rerun()

        except Exception as e:
            st.error("MCQ generation failed.")
            st.exception(e)

    # DISPLAY MCQS
    if chat["mcqs"]:
        st.divider()
        st.subheader("Quiz")

        # PDF
        try:
            pdf_bytes = generate_mcq_pdf(
                mcqs=chat["mcqs"],
                difficulty=difficulty,
                video_url=chat["video_url"]
            )

            st.download_button(
                label="📄 Download MCQ Quiz as PDF",
                data=pdf_bytes,
                file_name="youtube_mcq_quiz.pdf",
                mime="application/pdf",
                use_container_width=True,
                key=f"download_pdf_{chat['thread_id']}"
            )

        except Exception as e:
            st.error("Could not generate MCQ PDF.")
            st.exception(e)

        st.divider()

        # QUESTIONS
        selected_answers = {}
        for index, mcq in enumerate(chat["mcqs"]):
            st.markdown(f"### Question {index + 1}")
            st.write(mcq.question)

            selected_answers[index] = st.radio(
                "Choose your answer",
                [
                    f"A. {mcq.option_a}",
                    f"B. {mcq.option_b}",
                    f"C. {mcq.option_c}",
                    f"D. {mcq.option_d}",
                ],
                key=(
                    f"mcq_"
                    f"{chat['thread_id']}_"
                    f"{index}"
                ),
                index=None
            )
            st.divider()

        # SUBMIT QUIZ
        if st.button(
            "✅ Submit Quiz",
            type="primary",
            use_container_width=True,
            key=f"submit_quiz_{chat['thread_id']}"
        ):

            score = 0
            for index, mcq in enumerate(chat["mcqs"]):
                answer = selected_answers.get(index)
                if answer:
                    selected_letter = answer[0]
                    if selected_letter == mcq.correct_answer:
                        score += 1

            chat["quiz_submitted"] = True
            chat["score"] = score
            st.rerun()

        # RESULT
        if chat["quiz_submitted"]:
            score = chat["score"]
            total = len(chat["mcqs"])
            st.success(f"Your score: {score}/{total}")

            st.divider()
            st.subheader("Answers & Explanations")

            for index, mcq in enumerate(chat["mcqs"]):
                st.markdown(
                    f"### {index + 1}. "
                    f"{mcq.question}"
                )
                st.write(f"**Correct answer: {mcq.correct_answer}")
                st.info(mcq.explanation)

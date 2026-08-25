import uuid
import streamlit as st
from backend.assistant.youtube_assistant import YouTubeAssistant
from styles import load_css

# PAGE CONFIG
st.set_page_config(
    page_title="YouTube AI",
    page_icon="▶️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# LOAD CSS
load_css()

# SESSION STATE - ASSISTANT
if "assistant" not in st.session_state:
    st.session_state.assistant = YouTubeAssistant()

# SESSION STATE - CHATS
if "chats" not in st.session_state:
    first_chat_id = str(uuid.uuid4())
    st.session_state.chats = {
        first_chat_id: {
            "title": "New Chat",
            "thread_id": first_chat_id,
            "video_url": None,
            "video_id": None,
            "messages": []
        }
    }

    st.session_state.current_chat = first_chat_id

# HELPERS
def create_new_chat():
    chat_id = str(uuid.uuid4())
    st.session_state.chats[chat_id] = {
        "title": "New Chat",
        "thread_id": chat_id,
        "video_url": None,
        "video_id": None,
        "messages": []
    }

    st.session_state.current_chat = chat_id

def get_current_chat():
    return st.session_state.chats[st.session_state.current_chat]

def load_chat_video(chat):
    if not chat["video_url"]:
        return

    st.session_state.assistant.load_video(chat["video_url"])

# CURRENT CHAT
chat = get_current_chat()

# SIDEBAR
with st.sidebar:
    st.markdown("## ▶️ YouTube AI")

    # YOUTUBE VIDEO
    st.markdown("### YouTube Video")
    url = st.text_input(
        "YouTube URL",
        value=chat["video_url"] or "",
        placeholder="Paste YouTube URL here...",
        label_visibility="collapsed"
    )

    if st.button(
        "▶  Load Video",
        type="primary",
        use_container_width=True,
    ):
        if not url.strip():
            st.error( "Please enter a YouTube URL.")

        else:
            try:
                with st.spinner("Loading video..."):
                    video_id = st.session_state.assistant.load_video(url)
                    
                chat["video_url"] = url
                chat["video_id"] = video_id

                st.success("Video loaded successfully!")
                st.rerun()

            except Exception as e:
                st.error("Failed to load video.")
                st.exception(e)

    # NEW CHAT
    if st.button("＋  New Chat",use_container_width=True):
        create_new_chat()
        st.rerun()

    st.divider()

    # CHAT HISTORY
    st.markdown("### Chats")
    chat_items = list(st.session_state.chats.items())

    # Newest first
    chat_items.reverse()
    for cid, item in chat_items:

        title = item["title"]
        if not title.strip():
            title = "New Chat"

        if len(title) > 32:
            title = title[:32] + "..."

        is_current = (cid == st.session_state.current_chat)

        if is_current:
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

            if selected_chat["video_url"]:
                try:
                    with st.spinner("Loading video..."):
                        load_chat_video(selected_chat)
                except Exception as e:
                    st.error("Could not load this video's index.")
                    st.exception(e)
            st.rerun()

# MAIN HEADER
st.markdown(
    '<div class="main-title">'
    'YouTube Assistant'
    '</div>',
    unsafe_allow_html=True
)


# VIDEO
if chat["video_url"]:
    video_id = chat["video_id"]

    st.markdown('<div class="video-container">',unsafe_allow_html=True)
    st.video(f"https://www.youtube.com/watch?v={video_id}")
    st.markdown("</div>",unsafe_allow_html=True)

else:
    st.info(
        "👈 Paste a YouTube URL in the sidebar "
        "and click **Load Video** to start."
    )

# CHAT MESSAGES
for message in chat["messages"]:
    role = message["role"]
    content = message["content"]

    with st.chat_message(role):
        st.markdown(content)

# CHAT INPUT
question = st.chat_input("Ask anything about this video...")
if question:

    # CHECK VIDEO
    if not chat["video_url"]:
        st.warning("Please load a YouTube video first.")
        st.stop()

    # SAVE USER MESSAGE
    chat["messages"].append(
        {
            "role": "user",
            "content": question
        }
    )

    # CHAT TITLE
    if chat["title"] == "New Chat":
        chat["title"] = question[:40]

    # DISPLAY USER MESSAGE
    with st.chat_message("user"):
        st.markdown(question)

    # ASSISTANT RESPONSE
    with st.chat_message("assistant"):
        try:
            stream = (
                st.session_state.assistant.ask_stream(
                    question=question,
                    thread_id=chat["thread_id"]
                )
            )
            answer = st.write_stream(stream)

            # Save complete response
            chat["messages"].append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

        except Exception as e:
            st.error("Something went wrong.")
            st.exception(e)
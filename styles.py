import streamlit as st

def load_css():
    st.markdown(
        """
        <style>

        /* =========================================================
           GLOBAL
           ========================================================= */
        .stApp {
            background-color: rgba(0, 0, 0, 1);
            color: #ffffff;
        }

        /* =========================================================
           SIDEBAR
           ========================================================= */
        section[data-testid="stSidebar"] {
            background-color: #171717;
        }
        section[data-testid="stSidebar"] * {
            color: #eeeeee;
        }

        /* =========================================================
           MAIN TITLE
           ========================================================= */

        .main-title {
            font-size: 30px;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 3px;
        }

        .main-subtitle {
            font-size: 14px;
            color: #999999;
            margin-bottom: 25px;
        }

        /* =========================================================
           CHAT
           ========================================================= */

        [data-testid="stChatMessage"] {
            border-radius: 12px;
        }

        /* =========================================================
           SIDEBAR CHAT BUTTONS
           ========================================================= */

        section[data-testid="stSidebar"]
        .stButton > button {
            text-align: left;
            border: none;
            background-color: transparent;
            border-radius: 8px;
            color: #dddddd;
        }

        section[data-testid="stSidebar"]
        .stButton > button:hover {
            background-color: #2a2a2a;
        }

        /* =========================================================
           LOAD VIDEO BUTTON
           ========================================================= */

        section[data-testid="stSidebar"]
        button[kind="primary"] {
            background-color: #dc2626;
            color: #ffffff;
            border: none;
            border-radius: 8px;
            font-weight: 600;
        }

        section[data-testid="stSidebar"]
        button[kind="primary"]:hover {
            background-color: #1d4ed8;
            color: #ffffff;
        }

        /* =========================================================
           INPUT
           ========================================================= */

        [data-testid="stChatInput"] {
            border-radius: 12px;
        }

        /* =========================================================
           STATUS
           ========================================================= */

        .status-box {
            background-color: #171717;
            border: 1px solid #333333;
            border-radius: 10px;
            padding: 12px;
            margin-bottom: 20px;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )
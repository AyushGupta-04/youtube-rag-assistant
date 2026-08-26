import streamlit as st
def load_css():
    st.markdown(
        """
        <style>
        /* =====================================================
           GLOBAL
           ===================================================== */

        html,
        body,
        [data-testid="stApp"],
        [data-testid="stAppViewContainer"] {
            background-color: #212121 !important;
        }

        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 2rem !important;
        }


        /* =====================================================
           STREAMLIT HEADER
           ===================================================== */

        [data-testid="stHeader"] {
            background-color: #212121 !important;
        }


        /* =====================================================
           SIDEBAR
           ===================================================== */

        section[data-testid="stSidebar"] {
            background-color: #171717 !important;
        }

        section[data-testid="stSidebar"] * {
            color: #eeeeee;
        }


        /* =====================================================
           MAIN TITLE
           ===================================================== */

        .main-title {
            color: #ffffff;
            font-size: 30px;
            font-weight: 700;
            margin-bottom: 20px;
        }


        /* =====================================================
           YOUTUBE VIDEO
           ===================================================== */

        div.st-key-youtube_video {
            width: 70% !important;
            max-width: 760px !important;
            margin: 0 auto !important;
        }

        div.st-key-youtube_video [data-testid="stVideo"] {
            width: 100% !important;
        }


        /* =====================================================
           CHAT COMPOSER
           ===================================================== */

        div.st-key-chat_composer {
            background-color: #2f2f2f !important;
            border: 1px solid #4b4b4b !important;
            border-radius: 28px !important;
            min-height: 56px !important;
            padding: 6px 8px !important;
            margin-top: 18px !important;
            margin-bottom: 20px !important;
            box-sizing: border-box !important;
        }


        /* Remove container spacing */

        div.st-key-chat_composer > div {
            padding: 0 !important;
            margin: 0 !important;
        }


        /* =====================================================
           COLUMNS INSIDE COMPOSER
           ===================================================== */

        div.st-key-chat_composer
        div[data-testid="stHorizontalBlock"] {
            gap: 0 !important;
            align-items: center !important;
            padding: 0 !important;
            margin: 0 !important;
        }

        div.st-key-chat_composer
        div[data-testid="column"] {
            padding: 0 !important;
            margin: 0 !important;
        }


        /* =====================================================
           PLUS BUTTON
           ===================================================== */

        div.st-key-chat_composer
        div[data-testid="stPopover"] {
            width: 42px !important;
            min-width: 42px !important;
            height: 42px !important;
            margin: 0 !important;
            padding: 0 !important;
        }

        div.st-key-chat_composer
        div[data-testid="stPopover"] > div {
            width: 42px !important;
            height: 42px !important;
            margin: 0 !important;
            padding: 0 !important;
        }

        div.st-key-chat_composer
        div[data-testid="stPopover"] > div > button {
            width: 42px !important;
            height: 42px !important;
            min-width: 42px !important;
            min-height: 42px !important;

            padding: 0 !important;
            margin: 0 !important;

            border: none !important;
            border-radius: 50% !important;

            background: transparent !important;
            color: #eeeeee !important;

            font-size: 26px !important;
            font-weight: 300 !important;

            display: flex !important;
            align-items: center !important;
            justify-content: center !important;

            box-shadow: none !important;
            outline: none !important;
        }

        div.st-key-chat_composer
        div[data-testid="stPopover"] > div > button:hover {
            background-color: #414141 !important;
            color: #ffffff !important;
        }


        /* Hide popover arrow */

        div.st-key-chat_composer
        div[data-testid="stPopover"] > div > button svg {
            display: none !important;
        }


        /* =====================================================
           TEXT INPUT
           ===================================================== */

        div.st-key-chat_composer
        div[data-testid="stTextInput"] {
            width: 100% !important;
            margin: 0 !important;
            padding: 0 !important;
        }


        /* Hide label */

        div.st-key-chat_composer
        div[data-testid="stTextInput"] label {
            display: none !important;
        }


        /* Input wrapper */

        div.st-key-chat_composer
        div[data-testid="stTextInput"] > div {
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
            padding: 0 !important;
            margin: 0 !important;
        }


        /* Actual input */

        div.st-key-chat_composer
        div[data-testid="stTextInput"] input {
            width: 100% !important;
            height: 42px !important;

            background: transparent !important;
            color: #eeeeee !important;

            border: none !important;
            outline: none !important;
            box-shadow: none !important;

            font-size: 16px !important;

            padding: 0 8px !important;
            margin: 0 !important;
        }

        div.st-key-chat_composer
        div[data-testid="stTextInput"] input::placeholder {
            color: #9b9b9b !important;
            opacity: 1 !important;
        }

        div.st-key-chat_composer
        div[data-testid="stTextInput"] input:focus {
            background: transparent !important;
            border: none !important;
            outline: none !important;
            box-shadow: none !important;
        }


        /* =====================================================
           SEND BUTTON
           ===================================================== */

        div.st-key-chat_composer
        div[data-testid="stButton"] button {
            height: 40px !important;
            min-height: 40px !important;

            width: 40px !important;
            min-width: 40px !important;

            padding: 0 !important;
            margin: 0 auto !important;

            border: none !important;
            border-radius: 50% !important;

            background-color: #eeeeee !important;
            color: #222222 !important;

            font-size: 18px !important;
            font-weight: 700 !important;

            display: flex !important;
            align-items: center !important;
            justify-content: center !important;

            box-shadow: none !important;
        }

        div.st-key-chat_composer
        div[data-testid="stButton"] button:hover {
            background-color: #ffffff !important;
            color: #000000 !important;
        }


        /* =====================================================
           PLUS POPUP
           ===================================================== */

        div[data-testid="stPopoverBody"] {
            background-color: #2f2f2f !important;

            border: 1px solid #4a4a4a !important;
            border-radius: 14px !important;

            min-width: 230px !important;

            padding: 7px !important;

            box-shadow:
                0 12px 35px rgba(0, 0, 0, 0.5) !important;
        }


        /* Popup button */

        div[data-testid="stPopoverBody"]
        div[data-testid="stButton"] button {
            width: 100% !important;
            height: 44px !important;
            min-height: 44px !important;

            border: none !important;
            border-radius: 9px !important;

            background: transparent !important;
            color: #eeeeee !important;

            font-size: 14px !important;
            font-weight: 400 !important;

            text-align: left !important;
            justify-content: flex-start !important;

            padding: 8px 12px !important;

            box-shadow: none !important;
        }

        div[data-testid="stPopoverBody"]
        div[data-testid="stButton"] button:hover {
            background-color: #424242 !important;
            color: #ffffff !important;
        }


        /* =====================================================
           MCQ PAGE
           ===================================================== */

        .mcq-title {
            color: #ffffff;
            font-size: 28px;
            font-weight: 700;
            margin-bottom: 5px;
        }


        /* =====================================================
           MOBILE
           ===================================================== */

        @media (max-width: 768px) {

            .block-container {
                padding-left: 1rem !important;
                padding-right: 1rem !important;
            }

            div.st-key-chat_composer {
                border-radius: 24px !important;
            }

            div.st-key-youtube_video {
                width: 100% !important;
                max-width: none !important;
            }
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

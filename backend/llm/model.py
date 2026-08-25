from langchain_groq import ChatGroq
from backend.config.settings import GROQ_API_KEY


def create_llm():
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY not found.")

    try:
        return ChatGroq(
            model="openai/gpt-oss-20b",
            temperature=0.3,
            groq_api_key=GROQ_API_KEY
        )

    except Exception as e:
        raise RuntimeError(f"Failed to initialize ChatGroq: {e}") from e
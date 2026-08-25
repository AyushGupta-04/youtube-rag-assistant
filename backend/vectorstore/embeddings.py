from langchain_huggingface import HuggingFaceEndpointEmbeddings
from backend.config.settings import HF_TOKEN


def get_embed():
    if not HF_TOKEN:
        raise ValueError("HF_TOKEN not found in .env")

    try:
        return HuggingFaceEndpointEmbeddings(
            model="BAAI/bge-small-en-v1.5",
            huggingfacehub_api_token=HF_TOKEN
        )

    except Exception as e:
        raise RuntimeError(f"Failed to initialize HuggingFace embeddings: {e}") from e
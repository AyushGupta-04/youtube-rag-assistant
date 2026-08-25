from langchain_core.documents import Document
from langchain_community.document_loaders import YoutubeLoader

def yt_loader(url: str) -> list[Document]:
    try:
        loader = YoutubeLoader.from_youtube_url(url,language=["en", "hi"])
        docs = loader.load()

        if not docs:
            raise ValueError("No transcript found for this video.")

        return docs

    except Exception as e:
        raise RuntimeError(f"Failed to load YouTube transcript: {e}") from e
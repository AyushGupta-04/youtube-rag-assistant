from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def get_chunk( docs: list[Document] , chunk_size: int = 800, chunk_overlap: int = 150) ->list[Document]:
    if not docs:
        raise ValueError("No documents provided.")

    try:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

        return splitter.split_documents(docs)

    except Exception as e:
        raise RuntimeError( f"Failed to chunk transcript: {e}") from e
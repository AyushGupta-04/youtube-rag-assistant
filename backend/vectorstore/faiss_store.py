import os
from langchain_community.vectorstores import FAISS
from backend.youtube.url import get_video_id
from backend.youtube.loader import yt_loader
from backend.youtube.splitter import get_chunk


def get_vectorstore(url: str, embeddings) -> FAISS:
    video_id = get_video_id(url)
    index_path = os.path.join("faiss_indexes",video_id)
    index_file = os.path.join(index_path,"index.faiss")
    pickle_file = os.path.join(index_path,"index.pkl")

    try:
        # Existing FAISS
        if os.path.exists(index_file) and os.path.exists(pickle_file):
            print(f"Loading existing FAISS: {video_id}")

            return FAISS.load_local(
                index_path,
                embeddings=embeddings,
                allow_dangerous_deserialization=True
            )

        # Load transcript
        print("Loading YouTube transcript...")
        docs = yt_loader(url)

        # Chunk
        chunks = get_chunk(docs)

        # Metadata
        for  chunk in chunks:
            chunk.metadata["video_id"] = video_id
            chunk.metadata["video_url"] = url
        

        # Create FAISS
        vectorstore = FAISS.from_documents(documents=chunks,embedding=embeddings)

        # Save
        os.makedirs(index_path, exist_ok=True)
        vectorstore.save_local(index_path)

        print(f"FAISS saved at: {index_path}")
        return vectorstore

    except Exception as e:
        raise RuntimeError(f"Failed to create/load FAISS: {e}") from e
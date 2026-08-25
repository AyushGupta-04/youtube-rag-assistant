from langchain_community.vectorstores import FAISS

def create_retriever(vectorstore: FAISS):
    if vectorstore is None:
        raise ValueError("Vector store is required.")

    return vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 5,"fetch_k": 20}
    )
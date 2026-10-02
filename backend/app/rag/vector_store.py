from pathlib import Path

from langchain_chroma import Chroma

from app.rag.embeddings import embeddings


CHROMA_DIR = Path("data/chroma_db")


vector_store = Chroma(
    collection_name="ragops_documents",
    embedding_function=embeddings,
    persist_directory=str(CHROMA_DIR)
)
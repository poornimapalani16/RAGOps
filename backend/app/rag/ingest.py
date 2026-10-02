from pathlib import Path
from app.rag.loader import load_document
from app.rag.chunker import split_documents
from app.rag.vector_store import vector_store
def ingest_document(file_path: str):
    documents = load_document(file_path)
    chunks = split_documents(documents)
    file_name = Path(file_path).name
    ids = [
        f"{file_name}-{index}"
        for index in range(len(chunks))
    ]
    vector_store.add_documents(
        documents=chunks,
        ids=ids
    )
    return{
        "file": file_name,
        "documents": len(documents),
        "chunks": len(chunks)
    }
from pathlib import Path
from langchain_community.document_loaders import (
    PyMuPDFLoader,
    TextLoader,
    Docx2txtLoader,
    CSVLoader,
)
def load_document(file_path: str):
    path = Path(file_path)
    extension = path.suffix.lower()
    if extension == ".pdf":
        loader = PyMuPDFLoader(file_path)
    elif extension == ".txt":
        loader = TextLoader(
            file_path,
            encoding="utf-8"
        )
    elif extension == ".docx":
        loader = Docx2txtLoader(file_path)
    elif extension == ".csv":
        loader = CSVLoader(file_path)
    else:
        raise ValueError(
            f"Unsupported file type:{extension}"
        )        
    return loader.load()
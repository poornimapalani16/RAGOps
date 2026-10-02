from app.rag.vector_store import vector_store


retriever = vector_store.as_retriever(
    search_kwargs={
        "k": 2
    }
)


def retrieve_documents(query: str):

    return retriever.invoke(query)
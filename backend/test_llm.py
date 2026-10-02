from app.services.llm import llm


response = llm.invoke(
    "Explain RAG in one sentence."
)

print(response.content)
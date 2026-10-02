from app.graph.workflow import build_research_graph
graph= build_research_graph()
result = graph.invoke({
    "question":"Compare RAG and Fine-tuning for reducing hallucination in AI system."
})  
print("\n===== FINAL REPORT =====\n")
print(result["final_report"])
from langgraph.graph import StateGraph, START, END

from app.graph.state import ResearchState
from app.agents.planner import planner_node
from app.agents.researcher import researcher_node
from app.agents.verifier import verifier_node
from app.agents.synthesizer import synthesizer_node


def build_research_graph():

    graph = StateGraph(ResearchState)

    graph.add_node("planner", planner_node)
    graph.add_node("researcher", researcher_node)
    graph.add_node("verifier", verifier_node)
    graph.add_node("synthesizer", synthesizer_node)

    graph.add_edge(START, "planner")
    graph.add_edge("planner", "researcher")
    graph.add_edge("researcher", "verifier")
    graph.add_edge("verifier", "synthesizer")
    graph.add_edge("synthesizer", END)

    return graph.compile() 
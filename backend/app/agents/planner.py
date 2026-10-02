from app.services.llm import llm
from app.graph.state import ResearchState
from app.utils.llm_utils import get_response_text
from app.services.research_status import update_job


def planner_node(state: ResearchState):

    job_id = state["job_id"]
    question = state["question"]

    update_job(
        job_id,
        status="running",
        current_stage="planning",
    )

    prompt = f"""
You are the planning agent.

Research question:
{question}

Break this into exactly 3 focused research tasks.

Return only:
1. task
2. task
3. task

Keep each task short.
"""

    response = llm.invoke(prompt)

    response_text = get_response_text(response)

    tasks = [
        line.strip()
        for line in response_text.splitlines()
        if line.strip()
    ]

    # Never allow more than 3 tasks
    tasks = tasks[:3]

    update_job(
        job_id,
        current_stage="researching",
        completed_steps=1,
    )

    return {
        "research_tasks": tasks
    }
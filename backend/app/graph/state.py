from typing import TypedDict


class ResearchState(TypedDict, total=False):

    job_id: str

    question: str

    source_mode: str

    research_tasks: list[str]

    research_results: list[dict]

    verified_evidence: list[dict]

    final_report: str
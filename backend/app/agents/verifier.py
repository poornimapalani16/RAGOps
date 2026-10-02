import json

from app.services.llm import llm

from app.graph.state import ResearchState

from app.utils.llm_utils import (
    get_response_text
)

from app.models.evidence import (
    EvidenceItem
)

from app.services.research_status import (
    update_job
)

from app.utils.text_utils import (
    trim_text
)


def verify_task(
    task: str,
    web_sources: list,
    document_sources: list,
    source_mode: str
):

    prompt = f"""
You are an evidence verification agent.

Research task:
{task}

Source mode:
{source_mode}

Web sources:
{web_sources[:3]}

Document sources:
{document_sources[:2]}

IMPORTANT RULES:

1. Use ONLY the sources supplied above.
2. Do not invent a source.
3. Do not invent a URL.
4. Do not use knowledge outside the supplied sources.
5. A claim must be directly supported by the supplied source text.
6. Do not treat a source title alone as evidence.
7. Do not create numerical claims unless the supplied
   source text explicitly contains that number.
8. If the supplied sources do not support a claim,
   do not create that evidence item.
9. Return at most 2 evidence items.
10. Keep every field concise.

Return a JSON object:

{{
  "evidence": [
    {{
      "task": "short research task",
      "claim": "short factual claim",
      "evidence": "short supporting evidence",
      "source": {{
        "title": "source title",
        "url": "source URL or document source",
        "snippet": "short supporting source text",
        "source_type": "web"
      }},
      "verification": "supported",
      "confidence": 0.85
    }}
  ]
}}

Allowed verification values:

supported
partially_supported
conflicting
unsupported

If no source directly supports a claim,
return an empty evidence array.
"""


    response = llm.invoke_json(
        prompt
    )


    response_text = get_response_text(
        response
    )


    try:

        data = json.loads(
            response_text
        )

    except json.JSONDecodeError as error:

        raise ValueError(
            f"Groq returned invalid JSON: {error}"
        )


    items = data.get(
        "evidence",
        []
    )


    if not isinstance(
        items,
        list
    ):

        raise ValueError(
            "Verifier JSON must contain "
            "an evidence list."
        )


    verified_items = []


    for item in items[:2]:

        try:

            item["claim"] = trim_text(
                item.get(
                    "claim",
                    ""
                ),
                250
            )


            item["evidence"] = trim_text(
                item.get(
                    "evidence",
                    ""
                ),
                400
            )


            item["source"]["snippet"] = (
                trim_text(
                    item["source"].get(
                        "snippet",
                        ""
                    ),
                    400
                )
            )


            evidence = (
                EvidenceItem
                .model_validate(item)
            )


            verified_items.append(
                evidence.model_dump()
            )


        except Exception as error:

            print(
                "Skipping invalid evidence "
                f"item: {error}"
            )


    return verified_items


def verifier_node(
    state: ResearchState
):

    job_id = state["job_id"]

    research_results = (
        state["research_results"]
    )

    source_mode = state.get(
        "source_mode",
        "web_and_documents"
    )


    verified_evidence = []


    for research in research_results:

        task_evidence = verify_task(

            task=
                research["task"],

            web_sources=
                research.get(
                    "web_sources",
                    []
                ),

            document_sources=
                research.get(
                    "document_sources",
                    []
                ),

            source_mode=
                source_mode

        )


        verified_evidence.extend(
            task_evidence
        )


    verified_evidence = (
        verified_evidence[:6]
    )


    update_job(

        job_id,

        current_stage="synthesizing",

        completed_steps=3

    )


    return {

        "verified_evidence":
            verified_evidence

    }
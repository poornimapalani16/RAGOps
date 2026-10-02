from app.services.llm import llm
from app.graph.state import ResearchState
from app.utils.llm_utils import get_response_text


def synthesizer_node(state: ResearchState):

    question = state["question"]

    evidence = state[
        "verified_evidence"
    ]


    compact_evidence = []


    for item in evidence[:6]:

        compact_evidence.append({

            "claim":
                item["claim"],

            "evidence":
                item["evidence"],

            "source":
                item["source"],

            "verification":
                item["verification"],

            "confidence":
                item["confidence"]

        })


    prompt = f"""
You are a research report writer.

Question:
{question}

Verified evidence:
{compact_evidence}

Write a concise report.

Use exactly:

## Executive Summary

## Key Findings

## Evidence

## Sources

## Limitations

Use only the verified evidence.
Do not invent facts.
Do not invent sources.

Keep the report concise.
"""


    response = llm.invoke(prompt)


    return {
        "final_report":
            get_response_text(response)
    }
from typing import Literal

from pydantic import BaseModel, Field


class Source(BaseModel):

    title: str

    url: str

    snippet: str = ""

    source_type: Literal[
        "web",
        "document"
    ] = "web"


class EvidenceItem(BaseModel):

    task: str

    claim: str

    evidence: str

    source: Source

    verification: Literal[
        "supported",
        "partially_supported",
        "conflicting",
        "unsupported"
    ]

    confidence: float = Field(
        ge=0,
        le=1
    )
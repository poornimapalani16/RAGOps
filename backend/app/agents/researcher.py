from pathlib import Path

from app.graph.state import ResearchState

from app.tools.web_search import (
    web_search
)

from app.rag.retriever import (
    retrieve_documents
)

from app.services.research_status import (
    update_job
)

from app.utils.text_utils import (
    trim_text
)


def researcher_node(
    state: ResearchState
):

    job_id = state["job_id"]

    tasks = state["research_tasks"]

    source_mode = state.get(
        "source_mode",
        "web_and_documents"
    )


    results = []


    documents_dir = Path(
        "data/documents"
    )


    has_documents = (

        documents_dir.exists()

        and any(
            documents_dir.iterdir()
        )

    )


    for task in tasks:

        # =================================
        # Web Research
        # =================================

        web_sources = []


        if (
            source_mode ==
            "web_and_documents"
        ):

            web_response = web_search(
                task
            )


            for item in web_response.get(
                "results",
                []
            )[:3]:

                web_sources.append({

                    "title": trim_text(
                        item.get(
                            "title",
                            ""
                        ),
                        150
                    ),

                    "url": item.get(
                        "url",
                        ""
                    ),

                    "content": trim_text(
                        item.get(
                            "content",
                            item.get(
                                "snippet",
                                ""
                            )
                        ),
                        400
                    ),

                    "source_type":
                        "web"

                })


        # =================================
        # Local Document / RAG Research
        # =================================

        document_sources = []


        if has_documents:

            document_results = (
                retrieve_documents(task)
            )


            for doc in (
                document_results[:2]
            ):

                document_sources.append({

                    "content":
                        trim_text(
                            doc.page_content,
                            400
                        ),

                    "source":
                        trim_text(
                            str(
                                doc.metadata.get(
                                    "source",
                                    "uploaded document"
                                )
                            ),
                            150
                        ),

                    "source_type":
                        "document"

                })


        # =================================
        # Save compact research
        # =================================

        results.append({

            "task":
                task,

            "web_sources":
                web_sources,

            "document_sources":
                document_sources

        })


    update_job(

        job_id,

        current_stage="verifying",

        completed_steps=2

    )


    return {

        "research_results":
            results

    }
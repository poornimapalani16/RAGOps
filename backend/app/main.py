import os
from pathlib import Path
import shutil

from fastapi import (
    FastAPI,
    UploadFile,
    File,
    HTTPException,
    BackgroundTasks,
)

from fastapi.middleware.cors import CORSMiddleware

from pydantic import (
    BaseModel,
    Field,
)

from app.rag.ingest import ingest_document

from app.graph.workflow import (
    build_research_graph
)

from app.services.research_status import (
    create_job,
    update_job,
    get_job,
)


# =========================================
# FastAPI App
# =========================================

app = FastAPI(
    title="RAGOps API",
    description=(
        "Evidence-Driven Multi-Agent "
        "Research Assistant"
    ),
    version="1.0.0",
)


# =========================================
# CORS
# =========================================

origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "https://rag-b7dr3k31n-poornimapalani16-6966s-projects.vercel.app",
]


frontend_url = os.getenv(
    "FRONTEND_URL"
)


if frontend_url:

    origins.append(
        frontend_url
    )


app.add_middleware(

    CORSMiddleware,

    allow_origins=origins,

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


# =========================================
# Directories
# =========================================

UPLOAD_DIR = Path(
    "data/documents"
)


UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# =========================================
# Request Models
# =========================================

class ResearchRequest(BaseModel):

    question: str = Field(
        min_length=5,
        max_length=1000
    )

    source_mode: str = Field(
        default="web_and_documents"
    )


# =========================================
# Health
# =========================================

@app.get("/health")
async def health_check():

    return {

        "status": "ok",

        "service": "RAGOps API",

        "version": "1.0.0"

    }


# =========================================
# Root
# =========================================

@app.get("/")
async def root():

    return {

        "message":
            "Welcome to RAGOps API",

        "docs":
            "/docs",

        "health":
            "/health"

    }


# =========================================
# Document Upload
# =========================================

@app.post("/documents/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    allowed_extensions = {

        ".pdf",
        ".docx",
        ".txt",
        ".csv"

    }


    safe_filename = Path(
        file.filename or ""
    ).name


    if not safe_filename:

        raise HTTPException(
            status_code=400,
            detail="Invalid filename"
        )


    extension = Path(
        safe_filename
    ).suffix.lower()


    if extension not in allowed_extensions:

        raise HTTPException(

            status_code=400,

            detail=(
                "Unsupported file type. "
                "Allowed types: PDF, DOCX, "
                "TXT, CSV"
            )
        )


    file_path = (
        UPLOAD_DIR /
        safe_filename
    )


    try:

        with open(
            file_path,
            "wb"
        ) as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )


        result = ingest_document(
            str(file_path)
        )


        return {

            "message":
                "Document uploaded and "
                "indexed successfully",

            "details":
                result

        }


    except Exception as error:

        if file_path.exists():

            try:

                file_path.unlink()

            except OSError:

                pass


        raise HTTPException(

            status_code=500,

            detail=(
                "Document ingestion failed: "
                f"{str(error)}"
            )
        )


    finally:

        await file.close()


# =========================================
# Background Research
# =========================================

def run_research_job(
    job_id: str,
    question: str,
    source_mode: str
):

    try:

        graph = build_research_graph()


        result = graph.invoke({

            "job_id":
                job_id,

            "question":
                question,

            "source_mode":
                source_mode

        })


        update_job(

            job_id,

            status="completed",

            current_stage="completed",

            completed_steps=4,

            report=result.get(
                "final_report",
                ""
            ),

            evidence=result.get(
                "verified_evidence",
                []
            ),

            error=None

        )


    except Exception as error:

        update_job(

            job_id,

            status="failed",

            current_stage="failed",

            error=str(error)

        )


# =========================================
# Start Research
# =========================================

@app.post("/research")
async def research(

    request: ResearchRequest,

    background_tasks: BackgroundTasks,

):

    allowed_modes = {

        "web_and_documents",

        "documents_only"

    }


    if request.source_mode not in allowed_modes:

        raise HTTPException(

            status_code=400,

            detail=(
                "Invalid source mode. "
                "Use web_and_documents "
                "or documents_only."
            )
        )


    if (
        request.source_mode ==
        "documents_only"
    ):

        documents_exist = any(
            UPLOAD_DIR.iterdir()
        )


        if not documents_exist:

            raise HTTPException(

                status_code=400,

                detail=(
                    "Documents only mode "
                    "requires at least one "
                    "uploaded document."
                )
            )


    job = create_job(

        question=request.question,

        source_mode=request.source_mode

    )


    background_tasks.add_task(

        run_research_job,

        job["job_id"],

        request.question,

        request.source_mode

    )


    return {

        "job_id":
            job["job_id"],

        "status":
            "queued",

        "message":
            "Research started",

        "source_mode":
            request.source_mode

    }


# =========================================
# Research Status
# =========================================

@app.get(
    "/research/{job_id}"
)
async def research_status(
    job_id: str
):

    job = get_job(
        job_id
    )


    if job is None:

        raise HTTPException(

            status_code=404,

            detail="Research job not found"

        )


    return job
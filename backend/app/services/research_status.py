from threading import Lock
from uuid import uuid4


_jobs = {}

_lock = Lock()


def create_job(
    question: str,
    source_mode: str = "web_and_documents"
):

    job_id = str(uuid4())


    job = {

        "job_id": job_id,

        "question": question,

        "source_mode": source_mode,

        "status": "queued",

        "current_stage": "queued",

        "completed_steps": 0,

        "total_steps": 4,

        "report": "",

        "evidence": [],

        "error": None,
    }


    with _lock:

        _jobs[job_id] = job


    return job


def update_job(
    job_id: str,
    **updates
):

    with _lock:

        if job_id not in _jobs:

            return None


        _jobs[job_id].update(
            updates
        )


        return _jobs[job_id].copy()


def get_job(
    job_id: str
):

    with _lock:

        job = _jobs.get(
            job_id
        )


        if job is None:

            return None


        return job.copy()
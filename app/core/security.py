from fastapi import HTTPException
from app.core.limits import MAX_SUBMISSIONS


def enforce_submission_limit(count: int):
    if count >= MAX_SUBMISSIONS:
        raise HTTPException(
            status_code=429,
            detail="Submission limit reached. Await teacher review."
        )

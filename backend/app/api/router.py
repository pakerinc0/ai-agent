from fastapi import APIRouter


router = APIRouter()


@router.get("/status")
def status():
    return {
        "system": "AI Agent",
        "status": "running"
    }

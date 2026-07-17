from fastapi import FastAPI

from app.api.router import router
from app.core.config import settings


app = FastAPI(
    title=settings.PROJECT_NAME,
    version="0.1.0"
)


app.include_router(
    router,
    prefix="/api"
)


@app.get("/")
def root():
    return {
        "message": "AI Agent API is online"
    }


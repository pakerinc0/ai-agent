from fastapi import FastAPI
from app.api.router import router


app = FastAPI(
    title="AI Agent",
    description="Autonomous AI Agent Backend",
    version="0.1 Beta"
)


app.include_router(router)


@app.get("/")
async def health_check():
    return {
        "status": "running",
        "version": "beta"
    }

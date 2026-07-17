from fastapi import FastAPI

app = FastAPI(
    title="AI Agent API",
    description="Autonomous AI Agent backend",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "status": "online",
        "message": "AI Agent backend is running"
    }

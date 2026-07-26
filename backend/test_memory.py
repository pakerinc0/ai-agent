from app.memory.memory_manager import MemoryManager


memory = MemoryManager()


memory.remember(
    "создать FastAPI сервер",
    "использовать FastAPI и Uvicorn",
    "success"
)


result = memory.recall(
    "FastAPI"
)


print(result)

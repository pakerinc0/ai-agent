from app.memory.storage import MemoryStorage


memory = MemoryStorage()


memory.save(
    "Создать FastAPI сервер",
    {
        "status": "completed",
        "quality": 90
    }
)


print(
    memory.load()
)

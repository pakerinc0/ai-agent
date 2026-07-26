import asyncio

from app.core.worker import AgentWorker
from app.core.task_manager import TaskManager



async def main():


    manager = TaskManager()


    manager.add_task(
        "Создать простой Python калькулятор"
    )


    worker = AgentWorker()


    await worker.start()



if __name__ == "__main__":

    asyncio.run(main())

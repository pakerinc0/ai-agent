import asyncio


from app.core.agent_loop import AgentLoop
from app.core.task_manager import TaskManager



async def main():


    manager = TaskManager()


    manager.add_task(
        "Создать простой Python файл hello.py"
    )



    loop = AgentLoop()


    await loop.start()



asyncio.run(main())

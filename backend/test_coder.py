import asyncio

from app.agents.coder_agent import CoderAgent



async def main():

    agent = CoderAgent()


    result = await agent.run(
        "Создай простой FastAPI сервер"
    )


    print(result)



asyncio.run(main())

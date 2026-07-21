import asyncio

from app.agents.planner_agent import PlannerAgent



async def main():

    agent = PlannerAgent()


    result = await agent.run(
        "Создать Telegram бота на Python"
    )


    print(result)



asyncio.run(main())

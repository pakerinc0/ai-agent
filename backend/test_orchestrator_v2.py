import asyncio

from app.core.orchestrator import Orchestrator



async def main():


    agent = Orchestrator()


    result = await agent.execute(

        "Создай простой Python калькулятор"

    )


    print("\n===== RESULT =====")


    print(result)




asyncio.run(main())

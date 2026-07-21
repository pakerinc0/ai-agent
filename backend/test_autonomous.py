import asyncio

from app.core.orchestrator import Orchestrator



async def main():

    agent = Orchestrator()


    result = await agent.execute(

        """
Создай файл hello.py.

Внутри должна быть функция:

hello()

которая выводит:

Hello AI Agent

После создания запусти этот файл.
"""

    )


    print("\n===== RESULT =====")

    for key,value in result.items():

        print("\n###", key)

        print(value)



asyncio.run(main())

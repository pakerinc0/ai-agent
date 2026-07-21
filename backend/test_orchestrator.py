import asyncio

from app.core.orchestrator import Orchestrator



async def main():

    agent = Orchestrator()


    result = await agent.execute(
        """
Создай простой FastAPI сервис.

Требования:

1. Создать API сервер.
2. Добавить маршрут GET /hello.
3. Маршрут должен возвращать JSON:
{
    "message": "Hello AI"
}

4. Добавить обработку ошибок.
5. Код должен быть готов для запуска.
"""
    )


    print("\n========== RESULT ==========\n")


    for key, value in result.items():

        print("\n\n###", key)

        print(value)



if __name__ == "__main__":

    asyncio.run(main())

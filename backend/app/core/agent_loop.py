import asyncio

from app.core.engine import Engine


async def main():

    engine = Engine()

    result = await engine.execute(
        "Создай Python калькулятор"
    )

    print()

    print("========== RESULT ==========")

    print(result)


if __name__ == "__main__":

    asyncio.run(
        main()
    )

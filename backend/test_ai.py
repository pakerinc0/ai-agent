import asyncio

from app.ai.provider import ai


async def main():
    answer = await ai.generate(
        "Привет. Кто ты?"
    )

    print(answer)


asyncio.run(main())

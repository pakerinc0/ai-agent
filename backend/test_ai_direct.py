import asyncio

from app.ai.provider import ai


async def main():

    response = await ai.generate(
        """
Ответь только JSON:

{
    "test": "ok"
}
"""
    )


    print("===== AI RESPONSE =====")

    print(response)

    print("=======================")



asyncio.run(main())

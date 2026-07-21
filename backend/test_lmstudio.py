import asyncio

from app.ai.provider import ai



async def main():

    response = await ai.generate(
        """
Привет.
Ты сейчас работаешь как ядро AI агента.
Ответь одним предложением.
"""
    )


    print("\n=== AI RESPONSE ===\n")
    print(response)



if __name__ == "__main__":

    asyncio.run(main())

import asyncio

from app.agents.reviewer_agent import ReviewerAgent



async def main():

    agent = ReviewerAgent()


    code = """

def divide(a,b):

    return a/b


print(divide(5,0))

"""


    result = await agent.run(
        code
    )


    print(result)



asyncio.run(main())

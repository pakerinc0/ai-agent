import asyncio

from app.agents.tester_agent import TesterAgent



async def main():

    agent = TesterAgent()


    code = """

def login(password):

    if password == "12345":

        return True

    return False



print(login("12345"))

"""


    result = await agent.run(
        code
    )


    print(result)



asyncio.run(main())

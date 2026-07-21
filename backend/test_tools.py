import asyncio

from app.core.executor import AgentExecutor



async def main():

    executor = AgentExecutor()


    result = await executor.execute({

        "tool":"file",

        "method":"write_file",

        "params":{

            "path":"test_project/main.py",

            "content":"print('Hello AI Agent')"

        }

    })


    print(result)



asyncio.run(main())

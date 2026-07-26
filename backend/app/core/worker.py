import asyncio
from datetime import datetime

from app.core.agent_loop import AgentLoop
from app.core.task_manager import TaskManager



class AgentWorker:


    def __init__(self):

        self.tasks = TaskManager()

        self.agent = AgentLoop()

        self.running = False



    async def start(self):

        print("[WORKER] started")


        self.running = True


        while self.running:


            task = self.tasks.get_next_task()


            if task:


                print(
                    "[WORKER] executing:",
                    task["task"]
                )


                try:


                    result = await self.agent.run(
                        task["task"]
                    )


                    self.tasks.complete_task(
                        task["id"]
                    )


                    print(
                        "[WORKER] completed"
                    )


                    print(
                        result
                    )


                except Exception as e:


                    print(
                        "[WORKER] error:",
                        e
                    )



            else:


                print(
                    "[WORKER] no tasks"
                )


            await asyncio.sleep(
                5
            )





async def main():


    worker = AgentWorker()


    await worker.start()



if __name__ == "__main__":

    asyncio.run(main())

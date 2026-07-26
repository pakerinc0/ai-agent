from datetime import datetime

from app.memory.memory_manager import MemoryManager
from app.core.state import AgentState
from app.core.agent_manager import AgentManager


class Engine:

    def __init__(self):

        self.memory = MemoryManager()

        self.state = AgentState()

        self.manager = AgentManager()



    async def execute(
        self,
        task: str,
        plan,
        architecture
    ):

        print("[ENGINE] Task received")


        self.state.update_status(
            "working"
        )

        self.state.set_task(
            task
        )


        #
        # MEMORY SEARCH
        #

        print("[MEMORY] searching")


        memory = self.memory.search(
            task
        )


        if memory:
            print(
                "[MEMORY] previous experience found"
            )

        else:
            print(
                "[MEMORY] no experience"
            )



        #
        # CODER
        #

        print(
            "[CODER] started"
        )


        code = await self.manager.run_agent(
            "coder",
            task,
            {
                "plan": plan,
                "architecture": architecture
            }
        )


        print(
            "[CODER] completed"
        )



        #
        # REVIEW
        #

        print(
            "[REVIEWER] started"
        )


        review = await self.manager.run_agent(
            "reviewer",
            task,
            {
                "files": code
            }
        )


        print(
            "[REVIEWER] completed"
        )



        #
        # TEST
        #

        print(
            "[TESTER] started"
        )


        test = await self.manager.run_agent(
            "tester",
            task,
            {
                "files": code
            }
        )


        print(
            "[TESTER] completed"
        )



        #
        # SAVE EXPERIENCE
        #

        self.memory.add(

            task,

            {

                "stage":
                "completed",


                "plan":
                plan,


                "architecture":
                architecture,


                "code":
                code,


                "review":
                review,


                "test":
                test,


                "status":
                "success"

            }

        )



        self.state.update_status(
            "idle"
        )



        return {

            "task":
            task,


            "plan":
            plan,


            "architecture":
            architecture,


            "code":
            code,


            "review":
            review,


            "test":
            test,


            "memory":
            memory,


            "created":
            datetime.now().isoformat()

        }

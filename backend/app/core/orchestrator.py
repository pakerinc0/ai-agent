from app.core.agent_manager import AgentManager
from app.core.action_parser import ActionParser
from app.core.executor import AgentExecutor
from app.memory.memory_manager import MemoryManager



class Orchestrator:


    def __init__(self):

        self.manager = AgentManager()

        self.parser = ActionParser()

        self.executor = AgentExecutor()

        self.memory = MemoryManager()

        self.max_retries = 3



    async def execute(self, task: str):


        print("[ORCHESTRATOR] Task started")


        result = {

            "task": task,

            "steps": []

        }



        # =========================
        # MEMORY SEARCH
        # =========================


        print("[MEMORY] searching")


        old_memory = self.memory.search(
            task
        )


        result["memory"] = old_memory



        if old_memory:

            print(
                "[MEMORY] found:",
                len(old_memory)
            )

        else:

            print(
                "[MEMORY] empty"
            )




        # =========================
        # PLANNER
        # =========================


        planner = self.manager.get_agent(
            "planner"
        )


        plan = await planner.run(
            task
        )


        print(
            "[PLANNER] completed"
        )


        result["plan"] = plan





        # =========================
        # CODER
        # =========================


        coder = self.manager.get_agent(
            "coder"
        )


        coder_output = await coder.run(
            plan
        )


        print(
            "[CODER] generated"
        )


        print(
            "===== CODER RAW ====="
        )


        print(
            coder_output
        )


        print(
            "====================="
        )



        actions = self.parser.parse_all(
            coder_output
        )


        if not actions:


            return {

                "error":
                "Coder returned invalid actions",

                "raw":
                coder_output

            }



        print(
            "[ACTIONS PARSED]"
        )


        print(
            actions
        )




        # =========================
        # EXECUTION
        # =========================


        execution = await self.executor.execute(
            actions
        )


        print(
            "[EXECUTOR] finished"
        )


        result["execution"] = execution





        # =========================
        # REVIEW
        # =========================


        reviewer = self.manager.get_agent(
            "reviewer"
        )


        review = await reviewer.run(
            str(execution)
        )


        print(
            "[REVIEWER] completed"
        )


        result["review"] = review




        # =========================
        # SAVE MEMORY
        # =========================


        self.memory.add(

            task,

            {

                "execution": execution,

                "review": review

            }

        )


        print(
            "[MEMORY] saved"
        )




        result["final"] = execution


        result["final_review"] = review



        print(
            "[ORCHESTRATOR] finished"
        )


        return result

from app.core.agent_manager import AgentManager
from app.core.engine import Engine



class Orchestrator:


    def __init__(self):

        self.manager = AgentManager()

        self.engine = Engine()



    async def execute(
        self,
        task: str
    ):


        print(
            "[ORCHESTRATOR] Task started"
        )


        #
        # PLAN
        #

        plan = await self.manager.run_agent(
            "planner",
            task,
            {}
        )


        print(
            "[PLANNER] completed"
        )



        #
        # ARCHITECTURE
        #

        architecture = await self.manager.run_agent(

            "architect",

            task,

            {
                "plan": plan
            }

        )


        print(
            "[ARCHITECT] completed"
        )



        #
        # EXECUTION ENGINE
        #

        result = await self.engine.execute(

            task,

            plan,

            architecture

        )



        print(
            "[ORCHESTRATOR] finished"
        )



        return result

from app.agents.planner_agent import PlannerAgent
from app.agents.coder_agent import CoderAgent
from app.agents.reviewer_agent import ReviewerAgent
from app.agents.tester_agent import TesterAgent
from app.agents.debugger_agent import DebuggerAgent
from app.agents.tool_agent import ToolAgent
from app.agents.architect_agent import ArchitectAgent



class AgentManager:


    def __init__(self):

        self.agents = {

            "planner": PlannerAgent(),

            "architect": ArchitectAgent(),

            "coder": CoderAgent(),

            "reviewer": ReviewerAgent(),

            "tester": TesterAgent(),

            "debugger": DebuggerAgent(),

            "tool": ToolAgent(),

        }



    async def run_agent(
        self,
        name,
        task,
        context=None
    ):


        if name not in self.agents:

            raise Exception(
                f"Agent {name} not found"
            )


        if context is None:

            context = {}



        agent = self.agents[name]



        if name == "planner":


            result = await agent.run(

                task

            )



        elif name == "architect":


            result = await agent.run(

                context.get(
                    "plan"
                )

            )



        elif name == "coder":


            result = await agent.run(

                task,

                context.get(
                    "plan"
                ),

                context.get(
                    "architecture"
                )

            )



        elif name == "tester":


            result = await agent.run(

                task,

                {

                    "files":
                    context.get(
                        "files",
                        []
                    )

                }

            )



        elif name == "reviewer":


            result = await agent.run(

                task,

                {

                    "files":
                    context.get(
                        "files",
                        []
                    ),

                    "test":
                    context.get(
                        "test",
                        ""
                    )

                }

            )



        elif name == "debugger":


            result = await agent.run(

                context

            )



        elif name == "tool":


            result = await agent.run(

                context

            )



        else:


            result = await agent.run(

                task

            )



        return result

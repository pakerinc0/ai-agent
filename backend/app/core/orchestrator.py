from app.core.processor import Processor
from app.core.planner import Planner
from app.core.architect import Architect
from app.tools.registry import ToolRegistry


class Orchestrator:


    def __init__(self):

        self.processor = Processor()

        self.planner = Planner()

        self.architect = Architect()

        self.tools = ToolRegistry()



    async def execute(self, message):

        return self.run(message)



    def run(self, message):


        # 1. Анализ запроса

        analysis = self.processor.analyze(
            message
        )


        architecture = None



        # 2. Если задача создания проекта

        if analysis.get("intent") == "file_task":


            architecture = self.architect.design(
                message
            )



        # 3. Создание плана

        plan = self.planner.create_plan(
            analysis,
            architecture
        )



        # 4. Выполнение действия

        if plan.get("action") == "execute_tool":


            tool_name = plan.get(
                "tool"
            )


            tool = self.tools.get(
                tool_name
            )


            if tool is None:

                return {

                    "analysis": analysis,

                    "plan": plan,

                    "execution": {

                        "error":
                        f"Tool {tool_name} not found"

                    }

                }



            try:


                # проектный инструмент

                if tool_name == "project":


                    result = tool.create_project(
                        plan["params"]
                    )


                else:


                    result = tool.execute(
                        plan
                    )


            except Exception as e:


                result = {

                    "error":
                    str(e)

                }



            return {


                "analysis":
                analysis,


                "plan":
                plan,


                "execution":
                result

            }



        return {


            "analysis":
            analysis,


            "plan":
            plan,


            "execution":
            {

                "response":
                "No tool required"

            }

        }

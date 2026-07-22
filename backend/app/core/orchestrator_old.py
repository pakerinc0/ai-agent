from app.core.agent_manager import AgentManager
from app.core.action_parser import ActionParser
from app.core.executor import AgentExecutor



class Orchestrator:


    def __init__(self):

        self.manager = AgentManager()

        self.parser = ActionParser()

        self.executor = AgentExecutor()

        self.max_retries = 3



    async def execute(self, task: str):


        print("[ORCHESTRATOR] Task started")


        result = {

            "task": task,

            "steps": []

        }



        # =====================
        # PLANNER
        # =====================


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



        # =====================
        # CODER
        # =====================


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



        if not coder_output:


            return {

                "error":
                "Coder returned empty response"

            }



        # =====================
        # ACTION PARSER
        # =====================


        action = self.parser.parse(
            coder_output
        )



        if not action:


            return {

                "error":
                "Coder did not return valid action",

                "raw":
                coder_output

            }



        print(
            "[ACTION PARSED]"
        )


        print(
            action
        )



        # =====================
        # EXECUTOR
        # =====================


        execution = await self.executor.execute(
            action
        )


        print(
            "[EXECUTOR] finished"
        )



        result["execution"] = execution



        # =====================
        # REVIEWER
        # =====================


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



        # =====================
        # FIX LOOP
        # =====================


        attempt = 0



        while (

            "NEEDS_FIX" in review

            and

            attempt < self.max_retries

        ):


            attempt += 1


            print(
                f"[FIX] attempt {attempt}"
            )



            fix_prompt = f"""


Исправь результат.


Текущий результат:

{execution}


Ошибки проверки:

{review}


Верни только JSON action.


Формат:

{{
"tool":"file",
"method":"write_file",
"params":{{
"path":"file.py",
"content":"код"
}}
}}

"""


            coder_output = await coder.run(
                fix_prompt
            )



            print(
                "===== FIX CODER RAW ====="
            )


            print(
                coder_output
            )


            print(
                "========================="
            )



            action = self.parser.parse(
                coder_output
            )



            if action:


                execution = await self.executor.execute(
                    action
                )



            review = await reviewer.run(
                str(execution)
            )



        # =====================
        # FINAL
        # =====================


        result["final"] = execution

        result["final_review"] = review



        print(
            "[ORCHESTRATOR] finished"
        )



        return result

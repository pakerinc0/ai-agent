from app.core.agent_manager import AgentManager



class Orchestrator:


    def __init__(self):

        self.manager = AgentManager()

        self.max_retries = 3



    async def execute(self, task: str):


        print("[ORCHESTRATOR] Task started")


        result = {

            "task": task,

            "attempts": []

        }


        # ==========================
        # PLAN
        # ==========================


        planner = self.manager.get_agent(
            "planner"
        )


        plan = await planner.run(
            task
        )


        result["plan"] = plan


        print("[PLANNER] completed")



        # ==========================
        # CODER
        # ==========================


        coder = self.manager.get_agent(
            "coder"
        )


        code = await coder.run(
            plan
        )


        print("[CODER] generated")



        # ==========================
        # REVIEW LOOP
        # ==========================


        reviewer = self.manager.get_agent(
            "reviewer"
        )



        for attempt in range(
            self.max_retries
        ):


            print(
                f"[REVIEWER] attempt {attempt+1}"
            )



            review = await reviewer.run(
                code
            )



            result["attempts"].append({

                "code": code,

                "review": review

            })



            if "NEEDS_FIX" not in review:


                print(
                    "[REVIEWER] passed"
                )

                break



            print(
                "[CODER] fixing..."
            )



            fix_prompt = f"""


Исправь код.


Код:

{code}



Замечания Reviewer:

{review}



Верни новую версию.


"""


            code = await coder.run(
                fix_prompt
            )



        # ==========================
        # TEST
        # ==========================


        tester = self.manager.get_agent(
            "tester"
        )


        test = await tester.run(
            code
        )


        print("[TESTER] completed")



        result["final_code"] = code

        result["test"] = test



        return result

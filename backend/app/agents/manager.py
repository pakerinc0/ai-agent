from app.agents.architect import ArchitectAgent
from app.agents.coder import CoderAgent
from app.agents.project_builder import ProjectBuilderAgent
from app.agents.reviewer import ReviewerAgent

from app.ai.llm import LMStudioClient



class ManagerAgent:


    def __init__(self):


        # подключение к LM Studio
        self.llm = LMStudioClient()



        # агенты

        self.architect = ArchitectAgent(
            self.llm
        )


        self.coder = CoderAgent(
            self.llm
        )


        self.builder = ProjectBuilderAgent()


        self.reviewer = ReviewerAgent()



    async def execute(self, task: str):


        print(
            "\n[MANAGER] Starting task..."
        )



        # =========================
        # 1. Архитектор
        # =========================


        architecture = await self.architect.execute(
            task
        )



        if not architecture:


            return {

                "error":
                    "Architect returned empty result"

            }



        print(
            "[MANAGER] Architecture created"
        )



        # =========================
        # 2. Кодер
        # =========================


        code = await self.coder.execute(
            architecture
        )



        if not code:


            return {

                "error":
                    "Coder returned empty result"

            }



        files = code.get(
            "generated_files",
            []
        )



        print(
            f"[MANAGER] Generated files: {len(files)}"
        )



        # =========================
        # 3. Проверка кода
        # =========================


        review = await self.reviewer.execute(
            files
        )



        print(
            "[MANAGER] Code review finished"
        )



        # =========================
        # 4. Создание проекта
        # =========================


        build = await self.builder.execute(
            {

                "project_name":
                    architecture.get(
                        "project_name",
                        "generated_project"
                    ),


                "files":
                    files

            }
        )



        print(
            "[MANAGER] Project build finished"
        )



        return {


            "task":
                task,


            "architecture":
                architecture,


            "review":
                review,


            "build":
                build,


            "code":
                code

        }

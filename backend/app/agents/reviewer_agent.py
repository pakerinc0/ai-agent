from app.agents.base_agent import BaseAgent



class ReviewerAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "reviewer"
        )



    async def run(
        self,
        task,
        context
    ):


        files = context.get(
            "files"
        )

        test = context.get(
            "test"
        )



        prompt = f"""

Ты Senior Code Reviewer.


Задача:

{task}


Код:

{files}


Результаты тестов:

{test}



Проанализируй:

- архитектуру
- читаемость
- безопасность
- ошибки


Если всё хорошо:

GOOD


Если есть проблемы:

NEEDS_FIX


Ответ только анализ.
"""


        return await self.ai.generate(
            prompt
        )

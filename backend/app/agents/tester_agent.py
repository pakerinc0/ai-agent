from app.agents.base_agent import BaseAgent


class TesterAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "tester"
        )



    async def run(
        self,
        task,
        context
    ):


        files = context.get(
            "files",
            []
        )


        prompt = f"""
Ты Senior Python QA инженер.

Проверь настоящий код.

ЗАДАЧА:

{task}


ФАЙЛЫ:

{files}


Проверь:

1. Синтаксис
2. Логику
3. Ошибки выполнения
4. Крайние случаи


Ответ:

PASSED

или

FAILED

и список ошибок.
"""


        return await self.ai.generate(
            prompt
        )

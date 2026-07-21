from app.agents.base_agent import BaseAgent



class TesterAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "tester"
        )



    async def run(self, task: str):


        prompt = f"""
Ты являешься Tester Agent.

Твоя задача:
проверять программный код.

Анализируй:

- возможные ошибки выполнения;
- отсутствие обработки исключений;
- неправильную логику;
- проблемы с производительностью;
- сценарии, которые могут сломать программу.


Код для проверки:

{task}


Ответ должен содержать:


1. Найденные ошибки

2. Тестовые сценарии

3. Что нужно исправить

4. Итог:

PASSED

или

FAILED

"""


        result = await self.ask_ai(
            prompt
        )


        return result

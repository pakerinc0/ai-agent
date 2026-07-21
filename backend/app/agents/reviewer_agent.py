from app.agents.base_agent import BaseAgent



class ReviewerAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "reviewer"
        )



    async def run(self, task: str):


        prompt = f"""
Ты являешься Reviewer Agent.

Твоя задача:
проверять код и находить проблемы.

Проверяй:

- ошибки Python;
- неправильную архитектуру;
- плохие практики;
- потенциальные баги;
- безопасность;
- читаемость.


Задача:

{task}


Ответ должен иметь структуру:


1. Найденные проблемы

2. Почему это проблема

3. Как исправить

4. Итоговая оценка:
GOOD или NEEDS_FIX

"""


        result = await self.ask_ai(
            prompt
        )


        return result

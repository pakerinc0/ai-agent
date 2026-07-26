from app.agents.base_agent import BaseAgent


class PlannerAgent(BaseAgent):

    def __init__(self):
        super().__init__("planner")


    async def run(
        self,
        task,
        context=None
    ):

        prompt = f"""
Ты Senior Software Architect.

Создай подробный технический план выполнения задачи.

ЗАДАЧА:

{task}


Контекст:

{context}


Ответ должен содержать:

1. Анализ задачи
2. Этапы разработки
3. Возможные проблемы
4. Требования к коду
5. План тестирования


Пиши структурировано.
"""


        result = await self.ai.generate(
            prompt
        )


        return result

from app.agents.base_agent import BaseAgent



class PlannerAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "planner"
        )



    async def run(self, task: str):


        prompt = f"""
Ты являешься Planner Agent.

Твоя задача:
анализировать задачу пользователя
и создавать подробный план выполнения.

Не пиши код.
Только анализ и шаги.

Задача пользователя:

{task}


Создай структурированный план:
1.
2.
3.
"""


        result = await self.ask_ai(
            prompt
        )


        return result

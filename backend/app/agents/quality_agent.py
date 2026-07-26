from app.agents.base_agent import BaseAgent



class QualityAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "quality"
        )



    async def run(
        self,
        task: str
    ):


        prompt = f"""

Ты Quality Agent.

Твоя задача:
оценить качество программного решения.


Проверь:

1. Работает ли код.

2. Соответствует ли задаче.

3. Архитектура.

4. Читаемость.

5. Безопасность.

6. Производительность.


Выставь оценку от 0 до 100.


Ответ только JSON:


{{
"score": число,

"working": true или false,

"problems":[

"проблема 1",
"проблема 2"

],

"recommendation":
"что улучшить"

}}


Данные:

{task}


Только JSON.

"""


        result = await self.ask_ai(
            prompt
        )


        return result

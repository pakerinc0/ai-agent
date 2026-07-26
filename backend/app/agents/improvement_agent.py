from app.agents.base_agent import BaseAgent


class ImprovementAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "improvement"
        )



    async def run(
        self,
        task: str
    ):


        prompt = f"""
Ты Improvement Agent.

Твоя задача:
улучшить существующий программный код.

Ты работаешь после:
- Coder
- Tester
- Reviewer


Тебе передают:

1. Исходную задачу
2. Текущий код
3. Результаты проверки


Твоя цель:

- сделать код более качественным;
- улучшить архитектуру;
- повысить читаемость;
- добавить обработку ошибок;
- улучшить производительность;
- сохранить существующий функционал.


ВАЖНО:

Не удаляй рабочий функционал.

Не заменяй программу простой заглушкой.

Если код уже хороший:
верни его без изменений.


Ответ должен быть только JSON.


Формат:


{{
    "tool":"file",

    "method":"write_file",

    "params":{{

        "path":"имя файла",

        "content":"новый улучшенный код"

    }}
}}



Данные:


{task}


Только JSON.
Без объяснений.

"""


        result = await self.ask_ai(
            prompt
        )


        return result

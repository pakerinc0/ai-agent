from app.agents.base_agent import BaseAgent


class ArchitectAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "architect"
        )


    async def run(
        self,
        task,
        context=None
    ):

        plan = ""

        if isinstance(context, dict):

            plan = context.get(
                "plan",
                ""
            )


        prompt = f"""
Ты Senior Software Architect.

Твоя задача — создать техническую архитектуру проекта.


ЗАДАЧА:

{task}


ПЛАН:

{plan}


Создай подробное описание:


1. Структура проекта

Пример:

project/
 ├── app.py
 ├── modules/
 └── tests/


2. Файлы которые необходимо создать


Для каждого файла укажи:

- название
- назначение
- ответственность


3. Классы

Для каждого класса:

- имя
- файл
- методы
- назначение


4. Модули и зависимости


5. Поток выполнения программы


6. Возможные ошибки


7. План тестирования



Ответ должен быть структурированным.
Не пиши код.
"""


        result = await self.ai.generate(
            prompt
        )


        return result

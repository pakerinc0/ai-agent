from app.agents.base_agent import BaseAgent



class PlannerAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "planner"
        )



    async def run(
        self,
        task: str
    ):


        prompt = f"""
Ты являешься Planner Agent.

Проанализируй задачу:

{task}

Создай структурированный план.
Не пиши код.
"""


        result = await self.ask_ai(
            prompt
        )


        # если AI недоступен
        if (
            result.startswith(
                "LM Studio connection error"
            )
            or
            result.startswith(
                "Ollama connection error"
            )
        ):


            return self.local_plan(
                task
            )



        return result




    def local_plan(
        self,
        task
    ):


        return f"""
LOCAL PLANNER MODE


Задача:
{task}


План выполнения:


1. Анализ требований задачи.


2. Определение необходимых компонентов.


3. Разделение задачи на модули.


4. Создание структуры проекта.


5. Реализация основной логики.


6. Проверка работоспособности.


7. Исправление ошибок.


8. Сохранение результата в память агента.


Статус:
План создан без AI модели.
"""

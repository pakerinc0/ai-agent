from app.ai.provider import ai



class Planner:


    def __init__(self):

        pass



    async def create_plan(
            self,
            task: str
    ):


        try:


            prompt = f"""
Ты Planner Agent.

Проанализируй задачу.

Задача:
{task}


Создай подробный план выполнения:

1.
2.
3.
4.
5.

Не пиши код.
Только план.
"""


            result = await ai.generate(
                prompt
            )


            return result



        except Exception as e:


            print(
                "[PLANNER] LOCAL MODE"
            )


            return self.local_plan(
                task
            )




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


2. Определение компонентов системы.


3. Разделение задачи на модули.


4. Создание структуры проекта.


5. Реализация основной логики.


6. Проверка работоспособности.


7. Исправление ошибок.


8. Сохранение результата в память агента.



Статус:

План создан без AI модели.

"""

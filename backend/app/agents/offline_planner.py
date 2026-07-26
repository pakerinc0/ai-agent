class OfflinePlanner:


    name = "offline_planner"



    async def run(self, task):


        print(
            "[OFFLINE PLANNER]"
        )


        plan = f"""
План выполнения задачи:

Задача:
{task}


Шаги:

1. Проанализировать задачу.

2. Определить необходимые файлы.

3. Создать или изменить код.

4. Выполнить проверку.

5. Сохранить результат.

"""


        return plan

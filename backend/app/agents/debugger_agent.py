from app.agents.base_agent import BaseAgent



class DebuggerAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "debugger"
        )



    async def run(self, task: str):


        prompt = f"""

Ты Debugger Agent.


Твоя задача:

найти ошибку в программе
и создать исправленное действие.


Ты работаешь после Tester Agent.


Тебе передают:

- исходный код
- ошибку
- описание проблемы


Верни только JSON.


Если нужно изменить файл:


{{
"tool":"file",

"method":"write_file",

"params":{{

"path":"имя файла",

"content":"исправленный код"

}}

}}



Данные для исправления:


{task}


Только JSON.
Без объяснений.

"""


        result = await self.ask_ai(
            prompt
        )


        return result

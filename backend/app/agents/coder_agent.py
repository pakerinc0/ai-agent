from app.agents.base_agent import BaseAgent



class CoderAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "coder"
        )



    async def run(self, task: str):


        prompt = f"""

Ты автономный Coder Agent.

Ты управляешь компьютером через инструменты.

Твоя задача:
создать решение и выбрать действие.


ВАЖНО:

НЕ ПИШИ ОБЪЯСНЕНИЯ.

НЕ ПИШИ MARKDOWN.

НЕ ПИШИ ```.


Верни только JSON.


Создание файла:


{{
"tool":"file",
"method":"write_file",

"params":{{

"path":"hello.py",

"content":"тут код"

}}

}}



Запуск программы:


{{
"tool":"terminal",

"method":"run",

"params":{{

"command":"python hello.py"

}}

}}



Задача:


{task}


Ответ:
только JSON.

"""


        result = await self.ask_ai(
            prompt
        )


        return result

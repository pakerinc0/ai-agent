from app.agents.base_agent import BaseAgent


class CoderAgent(BaseAgent):


    def __init__(self):

        super().__init__("coder")



    async def run(self, task: str):


        prompt = f"""
Ты Coder Agent.

Ты создаёшь код для автономной системы.


ТВОЯ ЕДИНСТВЕННАЯ ЗАДАЧА:

Создать ОДИН файл.


НЕЛЬЗЯ:

- запускать программы
- создавать несколько действий
- писать объяснения
- использовать markdown
- использовать ``` 
- использовать """ + '"""' + """


Ответ строго JSON:


{
"tool":"file",
"method":"write_file",
"params":{
"path":"filename.py",
"content":"полный код здесь"
}
}



Правила:

1. Один ответ = один файл.
2. Код должен быть полностью готов.
3. Используй только обычные кавычки.
4. Не используй тройные кавычки.
5. Не запускай тесты.


Задача:

{task}


Ответ только JSON.
"""


        return await self.ask_ai(prompt)

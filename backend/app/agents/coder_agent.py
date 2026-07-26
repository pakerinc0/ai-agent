from app.agents.base_agent import BaseAgent
import json
import textwrap



class CoderAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "coder"
        )



    async def run(
        self,
        task: str
    ):


        prompt = f"""
Ты Coder Agent.

Твоя задача — создавать действия для выполнения задачи через инструменты.

Задача:

{task}


Ты работаешь через Tool System.

Возвращай ТОЛЬКО JSON.

Формат ответа:

{{
    "tool": "file",
    "method": "write_file",
    "params": {{
        "path": "filename.py",
        "content": "код файла"
    }}
}}


Правила:

- только JSON
- никаких markdown
- никаких ```python
- никаких объяснений
- используй только доступные инструменты
- для создания файлов используй:
  tool = file
  method = write_file
"""


        result = await self.ask_ai(
            prompt
        )


        if result:

            cleaned = self.clean_json(
                result
            )

            if cleaned:

                return cleaned



        print(
            "[CODER] LOCAL MODE"
        )


        return self.local_generate(
            task
        )




    def clean_json(
        self,
        text
    ):


        try:

            start = text.find("{")

            end = text.rfind("}") + 1


            if start == -1:

                return None



            data = text[start:end]


            json.loads(
                data
            )


            return data



        except Exception:

            return None





    def local_generate(
        self,
        task
    ):


        task_lower = task.lower()



        if "калькулятор" in task_lower:


            code = textwrap.dedent(
            """
            def add(a, b):
                return a + b


            def subtract(a, b):
                return a - b


            def multiply(a, b):
                return a * b


            def divide(a, b):

                if b == 0:
                    return None

                return a / b


            def main():

                print("Calculator")


            if __name__ == "__main__":
                main()
            """
            )



            return json.dumps(
            {
                "tool":
                    "file",

                "method":
                    "write_file",

                "params":
                {
                    "path":
                        "calculator.py",

                    "content":
                        code
                }
            },
            ensure_ascii=False
            )



        return json.dumps(
        {
            "tool":
                "file",

            "method":
                "write_file",

            "params":
            {
                "path":
                    "main.py",

                "content":
                    "print('Generated project')"
            }
        },
        ensure_ascii=False
        )

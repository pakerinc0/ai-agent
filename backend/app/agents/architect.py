import json


class ArchitectAgent:


    def __init__(self, llm):

        self.llm = llm



    async def execute(self, task: str):


        prompt = f"""
Ты архитектор программного обеспечения.

Твоя задача:
создать архитектуру настоящего проекта.

Пользовательская задача:

{task}


Верни ТОЛЬКО JSON.

Формат:

{{
    "project_name": "name",
    "description": "description",
    "folders": [
        "folder1",
        "folder2"
    ],
    "files": [
        {{
            "path": "src/main.py",
            "description": "что делает файл"
        }}
    ]
}}

ВАЖНО:
- НЕ пиши код.
- Только структура.
- Каждый файл должен иметь path и description.
"""



        response = await self.llm.generate(
            prompt
        )



        try:

            # если модель добавила текст вокруг JSON

            start = response.find("{")
            end = response.rfind("}") + 1


            json_text = response[start:end]


            architecture = json.loads(
                json_text
            )


            return architecture



        except Exception as e:


            return {

                "error": "Invalid JSON from architect",

                "raw": response,

                "exception": str(e)

            }

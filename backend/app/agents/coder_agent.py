import json
import re

from app.agents.base_agent import BaseAgent


class CoderAgent(BaseAgent):

    def __init__(self):
        super().__init__("coder")


    async def run(
        self,
        task,
        plan,
        architecture
    ):

        prompt = f"""
Ты Senior Python разработчик.

Создай рабочий код.

ЗАДАЧА:
{task}

ПЛАН:
{plan}

АРХИТЕКТУРА:
{architecture}


ОТВЕТ ТОЛЬКО JSON.

Формат:

{{
 "files": [
   {{
    "path":"main.py",
    "content":"код файла"
   }}
 ]
}}

ВАЖНО:

- Используй только двойные кавычки JSON.
- Никаких markdown.
- Никаких ```.
- Никаких тройных кавычек.
- content должен быть JSON строкой.
- Код должен быть полностью рабочим.
"""


        response = await self.ai.generate(
            prompt
        )


        print("[CODER RAW]")
        print(response)


        data = self.extract_json(response)


        files = data.get(
            "files",
            []
        )


        print(
            "[CODER] files:",
            len(files)
        )


        actions = []


        for file in files:

            if not isinstance(file, dict):
                continue


            path = file.get("path")
            content = file.get("content")


            if not path or not content:
                continue


            actions.append(
                {
                    "tool": "file",
                    "method": "write_file",
                    "params":
                    {
                        "path": path,
                        "content": content
                    }
                }
            )


        return actions



    def extract_json(
        self,
        text
    ):


        if isinstance(text, dict):
            return text



        cleaned = text.strip()


        cleaned = cleaned.replace(
            "```json",
            ""
        )

        cleaned = cleaned.replace(
            "```",
            ""
        )



        start = cleaned.find("{")

        end = cleaned.rfind("}")


        if start >= 0 and end >= 0:

            cleaned = cleaned[start:end+1]



        try:

            return json.loads(
                cleaned
            )


        except Exception:


            print(
                "[JSON REPAIR] trying repair"
            )


        try:


            # исправляем triple quotes модели

            cleaned = re.sub(
                r'"""(.*?)"""',
                lambda m:
                    json.dumps(
                        m.group(1)
                    ),
                cleaned,
                flags=re.S
            )


            cleaned = re.sub(
                r"'''(.*?)'''",
                lambda m:
                    json.dumps(
                        m.group(1)
                    ),
                cleaned,
                flags=re.S
            )


            return json.loads(
                cleaned
            )


        except Exception as e:


            print(
                "[CODER JSON ERROR]",
                e
            )


            return {
                "files":[]
            }

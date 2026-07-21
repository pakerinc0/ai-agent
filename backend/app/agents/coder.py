import json


class CoderAgent:


    def __init__(self, llm):

        self.llm = llm



    async def execute(self, architecture):


        files = architecture.get(
            "files",
            []
        )


        generated = []



        for file in files:


            # если файл пришел строкой
            if isinstance(file, str):

                path = file

                prompt = f"""
Создай содержимое файла:

{path}

Проект:
{architecture.get("description")}

Верни только код файла.
"""


                content = await self.llm.generate(
                    prompt
                )


            # если пришел объект
            elif isinstance(file, dict):


                path = file.get(
                    "path"
                )


                # если архитектор уже дал код

                if file.get("content"):

                    content = file["content"]


                else:

                    prompt = f"""
Создай код файла:

{path}

Описание:
{file.get("description","")}

Проект:
{architecture.get("description")}

Верни только код.
"""


                    content = await self.llm.generate(
                        prompt
                    )


            else:

                continue



            generated.append(
                {
                    "path": path,
                    "content": content
                }
            )



        return {

            "status": "success",

            "generated_files": generated

        }

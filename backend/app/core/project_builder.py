import os
import json
from datetime import datetime



class ProjectBuilder:


    def __init__(self):

        self.base_path = "projects"

        os.makedirs(
            self.base_path,
            exist_ok=True
        )



    def build(
            self,
            task,
            code
    ):


        project_name = self.make_name(
            task
        )


        project_path = os.path.join(
            self.base_path,
            project_name
        )


        os.makedirs(
            project_path,
            exist_ok=True
        )



        main_file = os.path.join(
            project_path,
            "main.py"
        )


        with open(
            main_file,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(
                code
            )



        readme = os.path.join(
            project_path,
            "README.md"
        )


        with open(
            readme,
            "w",
            encoding="utf-8"
        ) as f:


            f.write(
f"""# {task}


Автоматически создано AI Agent.


Дата:

{datetime.now().isoformat()}

"""
            )



        requirements = os.path.join(
            project_path,
            "requirements.txt"
        )


        with open(
            requirements,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(
                ""
            )



        result = {

            "status":
            "created",


            "project":
            project_name,


            "path":
            project_path,


            "files":
            [
                "main.py",
                "README.md",
                "requirements.txt"
            ],


            "time":
            datetime.now().isoformat()

        }


        return result




    def make_name(
            self,
            task
    ):


        name = task.lower()


        replace = [

            " ",
            "/",
            "\\",
            ":",
            ".",
            ","

        ]


        for char in replace:

            name = name.replace(
                char,
                "_"
            )


        return name[:50]

import os
import json
from datetime import datetime


class ProjectManager:

    def __init__(self):

        self.root = "workspace/projects"


        os.makedirs(
            self.root,
            exist_ok=True
        )


    def project_path(self, name):

        path = os.path.join(
            self.root,
            name
        )

        os.makedirs(
            path,
            exist_ok=True
        )

        return path



    def save_file(
        self,
        project,
        filename,
        content
    ):

        path = self.project_path(project)


        file_path = os.path.join(
            path,
            filename
        )


        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(content)


        return {
            "status":"saved",
            "file":file_path
        }




    def read_file(
        self,
        project,
        filename
    ):

        path = os.path.join(
            self.project_path(project),
            filename
        )


        if not os.path.exists(path):

            return None


        with open(
            path,
            encoding="utf-8"
        ) as f:

            return f.read()



    def list_files(
        self,
        project
    ):

        path = self.project_path(project)


        result=[]


        for root, dirs, files in os.walk(path):

            for file in files:

                result.append(
                    os.path.relpath(
                        os.path.join(root,file),
                        path
                    )
                )


        return result

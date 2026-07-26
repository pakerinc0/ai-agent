import os
from pathlib import Path


class FileManager:
    """
    Управление файлами проекта.
    """

    def __init__(self, root="workspace"):
        self.root = Path(root)

        self.root.mkdir(
            exist_ok=True
        )


    def normalize_path(
        self,
        path
    ):

        path = path.replace(
            "\\",
            "/"
        )

        path = path.lstrip(
            "/"
        )

        return self.root / path



    def write_file(
        self,
        path,
        content
    ):

        file_path = self.normalize_path(
            path
        )


        file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(
                content
            )


        return {
            "success": True,
            "file": str(file_path)
        }



    def read_file(
        self,
        path
    ):

        file_path = self.normalize_path(
            path
        )


        if not file_path.exists():

            return None


        return file_path.read_text(
            encoding="utf-8"
        )



    def exists(
        self,
        path
    ):

        return self.normalize_path(
            path
        ).exists()



    def list_files(self):

        result=[]


        for file in self.root.rglob("*"):

            if file.is_file():

                result.append(
                    str(
                        file.relative_to(
                            self.root
                        )
                    )
                )


        return result

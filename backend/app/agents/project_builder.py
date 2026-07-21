import os


class ProjectBuilderAgent:


    def __init__(self):
        pass



    async def execute(self, architecture):


        project_name = architecture.get(
            "project_name",
            "generated_project"
        )


        folders = architecture.get(
            "folders",
            []
        )


        files = architecture.get(
            "files",
            []
        )


        base = project_name


        created_files = []



        # =========================
        # Создание папок
        # =========================

        os.makedirs(
            base,
            exist_ok=True
        )


        for folder in folders:


            if isinstance(folder, dict):

                folder = (
                    folder.get("path")
                    or
                    folder.get("name")
                )


            if folder:


                os.makedirs(
                    os.path.join(
                        base,
                        folder
                    ),
                    exist_ok=True
                )



        # =========================
        # Создание файлов
        # =========================

        for item in files:



            file_path = None

            content = ""



            # Новый формат

            if isinstance(item, dict):


                file_path = (
                    item.get("path")
                    or
                    item.get("file_path")
                )


                content = item.get(
                    "content",
                    ""
                )



            # Старый формат

            elif isinstance(item, str):


                file_path = item



            if not file_path:

                continue



            full_path = os.path.join(
                base,
                file_path
            )



            directory = os.path.dirname(
                full_path
            )


            if directory:


                os.makedirs(
                    directory,
                    exist_ok=True
                )



            with open(
                full_path,
                "w",
                encoding="utf-8"
            ) as f:



                if isinstance(content, list):

                    f.write(
                        "\n".join(content)
                    )

                else:

                    f.write(
                        str(content)
                    )



            created_files.append(
                full_path
            )



        return {

            "status": "success",

            "project": project_name,

            "files_created": created_files

        }

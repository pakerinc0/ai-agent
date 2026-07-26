from app.core.file_manager import FileManager



class Executor:


    def __init__(self):

        self.files = FileManager()



    async def execute(
        self,
        project
    ):


        results=[]


        files = project.get(
            "files",
            []
        )


        for file in files:


            result=self.files.write_file(
                file["path"],
                file["content"]
            )


            results.append(
                result
            )



        return results

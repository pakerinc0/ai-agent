from app.core.project_manager import ProjectManager


class ProjectTool:

    name = "project"


    def __init__(self):

        self.manager = ProjectManager()



    def write_file(
        self,
        project,
        filename,
        content
    ):

        return self.manager.save_file(
            project,
            filename,
            content
        )



    def read_file(
        self,
        project,
        filename
    ):

        content = self.manager.read_file(
            project,
            filename
        )


        return {
            "file": filename,
            "content": content
        }



    def list_files(
        self,
        project
    ):

        return self.manager.list_files(
            project
        )

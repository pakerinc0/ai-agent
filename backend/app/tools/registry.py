from app.tools.system import SystemTool
from app.tools.file_tool import FileTool
from app.tools.project_tool import ProjectTool



class ToolRegistry:


    def __init__(self):

        self.tools = {


            "system_info":
                SystemTool(),


            "file":
                FileTool(),


            "project":
                ProjectTool()

        }



    def get(self,name):

        return self.tools.get(name)

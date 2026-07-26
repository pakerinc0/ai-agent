from app.tools.file_tool import FileTool
from app.tools.terminal_tool import TerminalTool
from app.tools.code_tool import CodeTool



class ToolRegistry:


    def __init__(self):

        self.tools={


            "file":
            FileTool(),


            "terminal":
            TerminalTool(),


            "code":
            CodeTool()

        }



    def get_tool(
        self,
        name
    ):

        return self.tools.get(name)



    def list_tools(self):

        return list(
            self.tools.keys()
        )

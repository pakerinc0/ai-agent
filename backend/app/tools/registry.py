from app.tools.system import SystemTool


class ToolRegistry:


    def __init__(self):

        self.tools = {

            "system_info": SystemTool()

        }



    def get(self, name):

        return self.tools.get(name)

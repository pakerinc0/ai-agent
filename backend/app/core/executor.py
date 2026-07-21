from app.core.tool_registry import ToolRegistry



class AgentExecutor:


    def __init__(self):

        self.tools = ToolRegistry()



    async def execute(self, action: dict):


        tool_name = action.get(
            "tool"
        )


        params = action.get(
            "params",
            {}
        )


        tool = self.tools.get_tool(
            tool_name
        )


        if not tool:

            return {
                "error": f"Tool {tool_name} not found"
            }


        method = action.get(
            "method"
        )


        function = getattr(
            tool,
            method,
            None
        )


        if not function:

            return {
                "error": "Method not found"
            }


        result = function(
            **params
        )


        return result

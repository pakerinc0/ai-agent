from app.agents.base_agent import BaseAgent
from app.core.tool_registry import ToolRegistry



class ToolAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "tool"
        )

        self.registry = ToolRegistry()



    async def run(self, action):


        tool_name = action.get(
            "tool"
        )


        method = action.get(
            "method"
        )


        params = action.get(
            "params",
            {}
        )



        tool = self.registry.get_tool(
            tool_name
        )



        if not tool:


            return {

                "error":
                f"Tool {tool_name} not found"

            }



        func = getattr(
            tool,
            method,
            None
        )



        if not func:


            return {

                "error":
                f"Method {method} not found"

            }



        return func(
            **params
        )

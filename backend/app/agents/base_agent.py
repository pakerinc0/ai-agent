from app.ai.provider import ai
from app.core.tool_registry import ToolRegistry



class BaseAgent:


    def __init__(self, name: str):

        self.name = name

        self.ai = ai

        self.tools = ToolRegistry()



    async def run(self, task: str):

        raise NotImplementedError(
            "Agent must implement run method"
        )



    async def ask_ai(self, prompt: str):

        result = await self.ai.generate(
            prompt
        )

        return result



    def use_tool(self, tool_name: str):

        return self.tools.get(
            tool_name
        )

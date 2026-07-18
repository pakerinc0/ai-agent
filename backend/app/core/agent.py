from datetime import datetime

from app.core.processor import Processor
from app.core.planner import Planner

from app.tools.registry import ToolRegistry

from app.ai.ollama import OllamaClient

from app.models.schemas import (
    Analysis,
    Plan,
    AgentResponse
)


class Agent:

    def __init__(self):

        self.name = "AI Agent"
        self.version = "0.3"

        self.processor = Processor()
        self.planner = Planner()
        self.tools = ToolRegistry()

        self.llm = OllamaClient()

        self.created_at = datetime.now()


    async def process(self, message: str):

        analysis = self.processor.analyze(message)

        plan = self.planner.create_plan(analysis)

        result = None


        if plan["action"] == "execute_tool":

            tool = self.tools.get(
                plan["tool"]
            )

            if tool:
                tool_result = await tool.execute()

                result = {
                    "success": True,
                    "data": tool_result,
                    "error": None
                }


        else:

            answer = await self.llm.generate(message)

            result = {
                "success": True,
                "data": {
                    "answer": answer,
                    "tool_result": None
                },
                "error": None
            }


        return AgentResponse(

            agent=self.name,

            version=self.version,

            input=message,

            analysis=Analysis(**analysis),

            plan=Plan(**plan),

            result=result,

            time=str(datetime.now())

        )

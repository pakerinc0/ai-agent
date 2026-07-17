from datetime import datetime

from app.core.processor import Processor
from app.core.planner import Planner

from app.tools.registry import ToolRegistry

from app.models.schemas import (
    Analysis,
    Plan,
    AgentResponse
)



class Agent:


    def __init__(self):

        self.name = "AI Agent"

        self.version = "0.1"


        self.processor = Processor()

        self.planner = Planner()

        self.tools = ToolRegistry()


        self.created_at = datetime.now()



    async def process(self, message: str):


        analysis = self.processor.analyze(
            message
        )


        plan = self.planner.create_plan(
            analysis
        )


        result = None



        if plan["action"] == "execute_tool":


            tool = self.tools.get(
                plan["tool"]
            )


            if tool:

                result = await tool.execute()



        return AgentResponse(

    agent=self.name,

    version=self.version,

    input=message,

    analysis=Analysis(**analysis),

    plan=Plan(**plan),

    result=result,

    time=str(datetime.now())

)

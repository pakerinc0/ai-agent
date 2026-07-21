from app.agents.planner_agent import PlannerAgent
from app.agents.coder_agent import CoderAgent
from app.agents.reviewer_agent import ReviewerAgent
from app.agents.tester_agent import TesterAgent
from app.agents.debugger_agent import DebuggerAgent
from app.agents.tool_agent import ToolAgent



class AgentManager:


    def __init__(self):


        self.agents = {


            "planner":
            PlannerAgent(),


            "coder":
            CoderAgent(),


            "reviewer":
            ReviewerAgent(),


            "tester":
            TesterAgent(),


            "debugger":
            DebuggerAgent(),


            "tool":
            ToolAgent()

        }



    def get_agent(self,name):

        return self.agents.get(name)



    def list_agents(self):

        return list(
            self.agents.keys()
        )

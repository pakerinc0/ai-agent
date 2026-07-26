from datetime import datetime

from app.memory.memory_manager import MemoryManager
from app.core.planner import Planner
from app.core.project_builder import ProjectBuilder
from app.core.state import AgentState


class Engine:

    def __init__(self):

        self.memory = MemoryManager()

        self.planner = Planner()

        self.builder = ProjectBuilder()

        self.state = AgentState()


    async def execute(
        self,
        task: str
    ):

        print("[ENGINE] Task received")

        self.state.update_status("working")
        self.state.set_task(task)

        print("[MEMORY] searching")

        memory = self.memory.search(task)

        if memory:
            print("[MEMORY] found previous experience")
        else:
            print("[MEMORY] no previous experience")

        print("[ENGINE] Planner started")

        plan = await self.planner.create_plan(task)

        print("[ENGINE] Planner finished")

        result = {

            "task": task,

            "plan": plan,

            "memory": memory,

            "created": datetime.now().isoformat()

        }

        self.memory.add(
            task,
            {
                "stage": "planning",
                "result": plan,
                "status": "success"
            }
        )

        self.state.update_status("idle")

        return result

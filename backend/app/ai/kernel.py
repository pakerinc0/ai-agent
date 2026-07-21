class AIKernel:

    def __init__(self):

        self.manager = None

    def register_manager(self, manager):

        self.manager = manager

    async def execute(self, task: str):

        if self.manager is None:

            raise RuntimeError(
                "Manager Agent not registered."
            )

        return await self.manager.execute(task)

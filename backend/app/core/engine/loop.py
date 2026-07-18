class AgentLoop:


    def __init__(self, processor, planner, tools, llm):

        self.processor = processor
        self.planner = planner
        self.tools = tools
        self.llm = llm



    async def run(self, message: str):

        # 1. Анализируем запрос

        analysis = self.processor.analyze(
            message
        )


        # 2. Создаём план

        plan = self.planner.create_plan(
            analysis
        )


        result = None



        # 3. Если нужен инструмент

        if plan["action"] == "execute_tool":


            tool = self.tools.get(
                plan["tool"]
            )


            if tool:

                result = await tool.execute()



        # 4. Если обычный разговор

        else:


            result = await self.llm.generate(
                message
            )


        return {
            "analysis": analysis,
            "plan": plan,
            "result": result
        }

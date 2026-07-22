from app.core.tool_registry import ToolRegistry



class AgentExecutor:


    def __init__(self):

        self.tools = ToolRegistry()





    async def execute(self, action):


        if isinstance(action, list):


            results = []


            for item in action:


                result = await self.execute_one(
                    item
                )


                results.append(
                    result
                )


            return results



        return await self.execute_one(
            action
        )






    async def execute_one(self, action):


        if not isinstance(action, dict):

            return {
                "error":
                "Invalid action format"
            }



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



        if not tool_name or not method:


            return {

                "error":
                "Missing tool or method"

            }





        tool = self.tools.get_tool(
            tool_name
        )



        if not tool:


            return {

                "error":
                f"Tool {tool_name} not found"

            }





        function = getattr(
            tool,
            method,
            None
        )



        if not function:


            return {

                "error":
                f"Method {method} not found"

            }





        try:


            result = function(
                **params
            )


            return {


                "tool":
                tool_name,


                "method":
                method,


                "status":
                "completed",


                "result":
                result


            }



        except Exception as e:


            return {


                "error":
                str(e)

            }

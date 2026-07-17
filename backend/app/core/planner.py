class Planner:


    def create_plan(self, analysis: dict):


        if analysis["intent"] == "system_check":

            return {

                "action": "execute_tool",

                "tool": "system_info"

            }


        return {

            "action": "generate_response"

        }

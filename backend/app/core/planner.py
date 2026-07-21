class Planner:



    def create_plan(
            self,
            analysis,
            architecture=None
    ):


        if analysis["intent"]=="file_task":


            return {


                "action":
                    "execute_tool",


                "tool":
                    "file"

            }



        if architecture:


            return {


                "action":
                    "execute_tool",


                "tool":
                    "project",


                "params":{


                    "path":
                        "generated_project",


                    "architecture":
                        architecture["architecture"]

                }

            }



        return {


            "action":
                "generate_response"

        }

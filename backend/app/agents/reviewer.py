class ReviewerAgent:


    def __init__(self):
        pass



    async def execute(self, files):

        problems = []


        for file in files:


            path = file.get("path")


            content = file.get("content")


            if not content:
                problems.append(
                    {
                        "file": path,
                        "problem": "Empty file"
                    }
                )


            if "TODO" in content:

                problems.append(
                    {
                        "file": path,
                        "problem": "Contains TODO"
                    }
                )


            if "import" not in content:

                problems.append(
                    {
                        "file": path,
                        "problem": "No imports detected"
                    }
                )



        return {


            "status":"review_finished",

            "problems":problems,

            "approved": len(problems)==0

        }

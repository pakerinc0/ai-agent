class OfflineCoder:


    name = "offline_coder"



    async def run(self, plan):


        print(
            "[OFFLINE CODER]"
        )


        action = {

            "tool":"file",

            "method":"write_file",

            "params":{

                "path":
                "offline_test.py",


                "content":
                """
print("Offline agent works")
"""

            }

        }


        return action

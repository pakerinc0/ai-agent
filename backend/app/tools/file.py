import os


class FileTool:


    def execute(self, params: dict):

        method = params.get("method")


        if method == "write_file":

            return self.write_file(
                params.get("path"),
                params.get("content")
            )


        return {
            "error": f"Unknown method: {method}"
        }



    def write_file(self, path, content):

        try:

            with open(
                path,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(content)


            return {

                "status": "success",

                "file": path,

                "message": "File created successfully"

            }


        except Exception as e:

            return {

                "status": "error",

                "message": str(e)

            }

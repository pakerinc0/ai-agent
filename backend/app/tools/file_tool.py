import os


class FileTool:


    name = "file"


    async def execute(self, **kwargs):

        method = kwargs.get("method")


        if method != "write_file":
            return {
                "error": f"Unsupported method: {method}"
            }


        path = kwargs.get("path")
        content = kwargs.get("content")


        if not path:
            return {
                "error": "path is required"
            }


        if content is None:
            return {
                "error": "content is required"
            }


        try:

            with open(
                path,
                "w",
                encoding="utf-8"
            ) as f:

                f.write(content)


            return {

                "success": True,

                "path": path,

                "message":
                    f"File {path} created"

            }


        except Exception as e:

            return {

                "success": False,

                "error": str(e)

            }

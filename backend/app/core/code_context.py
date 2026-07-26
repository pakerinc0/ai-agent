from pathlib import Path


class CodeContextExtractor:

    def __init__(self):
        pass


    def get_context(self, file_path: str):

        path = Path(file_path)


        if not path.exists():

            return {
                "status": "error",
                "message": f"File {file_path} not found"
            }


        try:

            content = path.read_text(
                encoding="utf-8"
            )


            return {

                "status": "success",

                "path": str(path),

                "size": len(content),

                "lines": len(
                    content.splitlines()
                ),

                "content": content

            }


        except Exception as e:

            return {

                "status": "error",

                "message": str(e)

            }

import os


class FileTool:


    name = "file"



    def write_file(
        self,
        path,
        content
    ):


        if not path:

            return {

                "success": False,

                "error":
                    "path is required"

            }



        if content is None:


            return {

                "success": False,

                "error":
                    "content is required"

            }





        try:


            directory = os.path.dirname(
                path
            )


            if directory:


                os.makedirs(
                    directory,
                    exist_ok=True
                )



            with open(

                path,

                "w",

                encoding="utf-8"

            ) as f:


                f.write(
                    content
                )



            return {


                "success": True,


                "path":
                    path,


                "message":
                    f"File {path} created"

            }




        except Exception as e:


            return {


                "success": False,


                "error":
                    str(e)

            }

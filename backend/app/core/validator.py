import ast


class CodeValidator:


    def validate_python(
        self,
        code
    ):

        try:

            ast.parse(
                code
            )


            return {
                "valid": True,
                "error": None
            }


        except SyntaxError as e:


            return {
                "valid":False,
                "error":
                    str(e)
            }



    def validate_files(
        self,
        files
    ):

        errors=[]


        for file in files:

            path=file.get(
                "path"
            )


            content=file.get(
                "content"
            )


            if not path:

                errors.append(
                    "missing path"
                )

                continue



            if not content:

                errors.append(
                    f"{path}: empty content"
                )

                continue



            if path.endswith(
                ".py"
            ):

                result=self.validate_python(
                    content
                )


                if not result["valid"]:

                    errors.append(
                        {
                            "file":path,
                            "error":
                                result["error"]
                        }
                    )


        return {
            "valid":
                len(errors)==0,

            "errors":
                errors
        }

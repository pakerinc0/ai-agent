import subprocess
import os



class TestRunner:



    def run_project(
            self,
            project_path
    ):


        main_file = os.path.join(
            project_path,
            "main.py"
        )


        if not os.path.exists(main_file):

            return {

                "status":
                "error",

                "message":
                "main.py not found"

            }



        try:


            result = subprocess.run(

                [
                    "python",
                    main_file
                ],


                input="2\n+\n3\n",


                text=True,


                capture_output=True,


                timeout=10

            )


            return {


                "status":
                "success"
                if result.returncode == 0
                else "failed",


                "stdout":
                result.stdout,


                "stderr":
                result.stderr,


                "code":
                result.returncode

            }



        except Exception as e:


            return {


                "status":
                "error",


                "message":
                str(e)

            }

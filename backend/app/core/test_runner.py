import subprocess
import os



class TestRunner:


    def run_file(
        self,
        file_path
    ):


        if not os.path.exists(file_path):

            return {

                "status": "error",

                "message":
                    f"{file_path} not found"

            }



        try:


            result = subprocess.run(

                [
                    "python",
                    file_path
                ],

                text=True,

                capture_output=True,

                timeout=15

            )


            return {


                "status":
                    "passed"
                    if result.returncode == 0
                    else "failed",


                "stdout":
                    result.stdout,


                "stderr":
                    result.stderr,


                "return_code":
                    result.returncode


            }



        except subprocess.TimeoutExpired:


            return {

                "status":
                    "failed",

                "error":
                    "Execution timeout"

            }



        except Exception as e:


            return {


                "status":
                    "error",

                "error":
                    str(e)

            }

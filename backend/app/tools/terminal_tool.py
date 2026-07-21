import subprocess



class TerminalTool:



    def run(self, command):


        try:


            result = subprocess.run(

                command,

                shell=True,

                capture_output=True,

                text=True,

                timeout=30

            )


            return {


                "status":"completed",

                "stdout":
                result.stdout,


                "stderr":
                result.stderr,


                "code":
                result.returncode


            }



        except Exception as e:


            return {


                "status":"error",

                "message":
                str(e)

            }

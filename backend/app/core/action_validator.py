class ActionValidator:


    def validate(self, action):

        if not isinstance(action, dict):
            return False, "Action is not dict"


        if "tool" not in action:
            return False, "Missing tool"


        if "method" not in action:
            return False, "Missing method"


        if "params" not in action:
            return False, "Missing params"



        tool = action["tool"]
        method = action["method"]
        params = action["params"]



        if tool == "file":


            if method == "write_file":

                if "path" not in params:
                    return False, "Missing file path"


                if "content" not in params:
                    return False, "Missing file content"



        return True, "OK"

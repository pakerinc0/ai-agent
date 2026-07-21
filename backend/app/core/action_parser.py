import json
import re


class ActionParser:


    def parse(self, text):

        if not text:
            return None


        text = self.clean(text)


        decoder = json.JSONDecoder()


        start = 0


        while True:

            start = text.find("{", start)


            if start == -1:
                break


            try:

                data, _ = decoder.raw_decode(
                    text[start:]
                )


                action = self.normalize(data)


                if action:
                    return action


            except Exception:
                pass


            start += 1


        return None



    def clean(self, text):

        # убираем markdown блоки

        text = re.sub(
            r"```json",
            "",
            text,
            flags=re.IGNORECASE
        )


        text = text.replace(
            "```",
            ""
        )


        # LLM часто использует Python triple quotes
        # вместо JSON строк

        text = text.replace(
            '"""',
            '"'
        )


        return text.strip()



    def normalize(self, data):

        if not isinstance(data, dict):
            return None



        tool_data = data.get("tool")



        # ===============================
        # Формат:
        #
        # {
        #   "tool":"file",
        #   "method":"write_file",
        #   "params":{}
        # }
        #
        # ===============================


        if isinstance(tool_data, str):

            return {

                "tool": tool_data,

                "method": data.get(
                    "method"
                ),

                "params": data.get(
                    "params",
                    {}
                )

            }



        # ===============================
        # Формат:
        #
        # {
        #   "tool":{
        #       "name":"file",
        #       "method":"write_file"
        #   }
        # }
        #
        # ===============================


        if isinstance(tool_data, dict):


            tool_name = (

                tool_data.get(
                    "type"
                )

                or

                tool_data.get(
                    "name"
                )

                or

                tool_data.get(
                    "tool"
                )

            )


            method = (

                tool_data.get(
                    "method"
                )

                or

                data.get(
                    "method"
                )

            )


            params = (

                tool_data.get(
                    "params"
                )

                or

                data.get(
                    "params",
                    {}
                )

            )


            if tool_name:

                return {

                    "tool": tool_name,

                    "method": method,

                    "params": params

                }



        # ===============================
        # Формат:
        #
        # {
        #   "file":{
        #       "path":"hello.py"
        #   }
        # }
        #
        # ===============================


        if "file" in data:

            return {

                "tool": "file",

                "method":
                    data.get(
                        "method",
                        "write_file"
                    ),

                "params":
                    data.get(
                        "file"
                    )

            }



        return None

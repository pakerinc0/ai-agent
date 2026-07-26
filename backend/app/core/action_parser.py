import json
import re


class ActionParser:


    def clean(self, text):

        if not text:
            return ""

        text = text.strip()


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


        return text.strip()



    def parse(self, text):

        actions = self.parse_all(text)

        if actions:
            return actions[0]

        return None



    def parse_all(self, text):

        text = self.clean(text)


        if not text:
            return []


        print(
            f"[PARSER] Raw length: {len(text)}"
        )


        actions = []



        # ==================================
        # Попытка полного JSON
        # ==================================

        try:

            data = json.loads(text)


            actions.extend(
                self.extract_actions(data)
            )


            if actions:
                return actions


        except Exception:
            pass




        # ==================================
        # Поиск всех JSON объектов
        # ==================================

        decoder = json.JSONDecoder()


        index = 0


        while index < len(text):

            try:

                start = text.find(
                    "{",
                    index
                )


                if start == -1:
                    break



                data, end = decoder.raw_decode(
                    text[start:]
                )


                actions.extend(
                    self.extract_actions(data)
                )


                index = start + end



            except Exception:


                index = index + 1




        if actions:

            return actions




        # ==================================
        # Regex fallback
        # ==================================

        return self.regex_fallback(
            text
        )




    def extract_actions(
        self,
        data
    ):

        result = []


        if isinstance(
            data,
            list
        ):


            for item in data:

                action = self.normalize(
                    item
                )

                if action:

                    result.append(
                        action
                    )



        elif isinstance(
            data,
            dict
        ):


            action = self.normalize(
                data
            )

            if action:

                result.append(
                    action
                )


        return result





    def regex_fallback(
        self,
        text
    ):

        actions = []


        blocks = re.findall(
            r'\{.*?\}',
            text,
            re.DOTALL
        )


        for block in blocks:

            try:

                data = json.loads(
                    block
                )


                action = self.normalize(
                    data
                )


                if action:

                    actions.append(
                        action
                    )


            except Exception:

                pass



        return actions





    def normalize(
        self,
        data
    ):


        if not isinstance(
            data,
            dict
        ):

            return None



        tool = data.get(
            "tool"
        )


        if not tool:

            return None




        params = {}



        if isinstance(
            data.get("params"),
            dict
        ):

            params.update(
                data["params"]
            )




        for key in [

            "path",

            "content",

            "filename"

        ]:


            if key in data:

                params[key] = data[key]




        if isinstance(
            tool,
            dict
        ):


            tool_name = tool.get(
                "name"
            )


            method = (
                data.get("method")
                or
                tool.get("method")
            )


        else:


            tool_name = tool


            method = data.get(
                "method"
            )




        return {


            "tool":
                tool_name,


            "method":
                method,


            "params":
                params

        }

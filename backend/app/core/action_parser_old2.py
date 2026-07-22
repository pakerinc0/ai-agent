import json
import re



class ActionParser:


    def parse(self, text):

        if not text:
            return None


        text = self.clean(text)



        decoder = json.JSONDecoder()



        # ищем JSON массив

        start = text.find("[")


        if start != -1:

            try:

                data, _ = decoder.raw_decode(
                    text[start:]
                )


                actions = self.normalize_list(
                    data
                )


                if actions:

                    return actions


            except Exception:

                pass




        # если модель вернула один объект

        start = text.find("{")



        if start != -1:


            try:

                data, _ = decoder.raw_decode(
                    text[start:]
                )


                action = self.normalize(
                    data
                )


                if action:

                    return [action]


            except Exception:

                pass



        return None




    def clean(self,text):


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


        text = text.replace(
            '"""',
            '"'
        )


        return text.strip()





    def normalize_list(self,data):


        if not isinstance(data,list):

            return None



        result = []



        for item in data:


            action = self.normalize(
                item
            )


            if action:

                result.append(
                    action
                )



        return result





    def normalize(self,data):


        if not isinstance(data,dict):

            return None



        tool = data.get(
            "tool"
        )



        if isinstance(tool,str):


            return {


                "tool":
                tool,


                "method":
                data.get(
                    "method"
                ),


                "params":
                data.get(
                    "params",
                    {}
                )

            }



        return None

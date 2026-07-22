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



        # =========================
        # Попытка обычного JSON
        # =========================


        try:

            data = json.loads(text)


            if isinstance(data, list):

                for item in data:

                    action = self.normalize(item)

                    if action:
                        actions.append(action)


            else:

                action = self.normalize(data)

                if action:
                    actions.append(action)



            if actions:

                return actions


        except Exception:

            pass




        # =========================
        # Поиск JSON объектов
        # =========================


        objects = re.findall(
            r"\{.*?\}",
            text,
            re.DOTALL
        )


        for obj in objects:


            try:

                data = json.loads(
                    obj
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




        if actions:

            return actions





        # =========================
        # FIX для """ и '''
        # =========================


        tool = re.search(
            r'"tool"\s*:\s*"([^"]+)"',
            text
        )


        method = re.search(
            r'"method"\s*:\s*"([^"]+)"',
            text
        )


        path = re.search(
            r'"path"\s*:\s*"([^"]+)"',
            text
        )


        content = re.search(
            r'"content"\s*:\s*(?:"""|\'\'\')(.*?)(?:"""|\'\'\')',
            text,
            re.DOTALL
        )



        if tool and method:


            params = {}


            if path:

                params["path"] = path.group(1)



            if content:

                params["content"] = content.group(1)



            actions.append({

                "tool":
                    tool.group(1),

                "method":
                    method.group(1),

                "params":
                    params

            })



        return actions




    def normalize(self, data):


        if not isinstance(data, dict):

            return None



        tool = data.get(
            "tool"
        )


        if isinstance(tool, str):


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



        if isinstance(tool, dict):


            return {

                "tool":
                    tool.get(
                        "name"
                    )
                    or
                    tool.get(
                        "type"
                    ),

                "method":
                    tool.get(
                        "method"
                    )
                    or
                    data.get(
                        "method"
                    ),

                "params":
                    tool.get(
                        "params",
                        {}
                    )
                    or
                    data.get(
                        "params",
                        {}
                    )

            }



        return None

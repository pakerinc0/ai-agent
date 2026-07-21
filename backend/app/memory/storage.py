import json
import os
from datetime import datetime


class MemoryStorage:


    def __init__(self):

        self.file = "app/memory/memory.json"


        if not os.path.exists(self.file):

            with open(
                self.file,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    [],
                    f,
                    ensure_ascii=False,
                    indent=4
                )



    def save(
        self,
        task: str,
        result: dict
    ):


        memory = self.load()


        entry = {

            "time": datetime.now().isoformat(),

            "task": task,

            "result": result

        }


        memory.append(entry)


        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:


            json.dump(
                memory,
                f,
                ensure_ascii=False,
                indent=4
            )



    def load(self):


        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

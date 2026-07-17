import json
import os
from datetime import datetime


class Memory:

    def __init__(self, user_id: str):

        self.user_id = user_id

        self.folder = "app/services/memory_storage"

        os.makedirs(
            self.folder,
            exist_ok=True
        )

        self.file_path = (
            f"{self.folder}/{self.user_id}.json"
        )


        if not os.path.exists(self.file_path):

            with open(
                self.file_path,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    [],
                    file
                )


    def save(
        self,
        user_message: str,
        agent_response: str
    ):

        history = self.get_history()


        history.append({

            "user": user_message,

            "agent": agent_response,

            "time": str(datetime.now())

        })


        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                history,
                file,
                ensure_ascii=False,
                indent=4
            )



    def get_history(self):

        with open(
            self.file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

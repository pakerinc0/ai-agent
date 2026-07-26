import json
import os
import datetime



class AgentState:


    def __init__(self):


        self.file = "app/database/agent_state.json"


        os.makedirs(
            "app/database",
            exist_ok=True
        )


        if not os.path.exists(self.file):

            self.save({

                "status": "idle",

                "current_task": None,

                "current_agent": None,

                "stage": None,

                "errors": 0,

                "attempts": 0,

                "last_action": None,

                "last_result": None,

                "history": []

            })



    def save(self, data):


        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:


            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )



    def load(self):


        try:

            with open(
                self.file,
                "r",
                encoding="utf-8"
            ) as f:


                return json.load(f)


        except Exception:


            return {}




    def update(self, key, value):


        data = self.load()


        data[key] = value


        data["updated"] = (
            datetime.datetime.now()
            .isoformat()
        )


        self.save(data)





    def update_status(self, status):


        self.update(
            "status",
            status
        )





    def set_task(self, task):


        data = self.load()


        data["current_task"] = task


        data["history"].append({

            "task": task,

            "time":
            datetime.datetime.now()
            .isoformat()

        })


        self.save(data)





    def set_agent(self, agent):


        self.update(
            "current_agent",
            agent
        )





    def set_stage(self, stage):


        self.update(
            "stage",
            stage
        )





    def add_error(self):


        data = self.load()


        data["errors"] += 1


        self.save(data)





    def add_attempt(self):


        data = self.load()


        data["attempts"] += 1


        self.save(data)





    def save_action(self, action):


        self.update(
            "last_action",
            action
        )





    def save_result(self, result):


        self.update(
            "last_result",
            result
        )





    def reset(self):


        self.save({

            "status": "idle",

            "current_task": None,

            "current_agent": None,

            "stage": None,

            "errors": 0,

            "attempts": 0,

            "last_action": None,

            "last_result": None,

            "history": []

        })





    def get_state(self):


        return self.load()

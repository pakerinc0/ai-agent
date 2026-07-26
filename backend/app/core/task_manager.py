import json
import os
from datetime import datetime



class TaskManager:


    def __init__(self):

        self.file = "app/database/tasks.json"


        os.makedirs(
            "app/database",
            exist_ok=True
        )


        if not os.path.exists(
            self.file
        ):

            self.save([])



    def save(
        self,
        data
    ):

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

        except:

            return []



    def add_task(
        self,
        task
    ):


        tasks = self.load()


        task_id = len(tasks) + 1


        new_task = {


            "id":
            task_id,


            "task":
            task,


            "status":
            "waiting",


            "created":
            datetime.now().isoformat(),


            "finished":
            None

        }



        tasks.append(
            new_task
        )


        self.save(
            tasks
        )


        return new_task




    def get_next_task(
        self
    ):


        tasks = self.load()



        for task in tasks:


            if task["status"] == "waiting":


                task["status"] = "running"


                self.save(
                    tasks
                )


                return task



        return None




    def complete_task(
        self,
        task_id
    ):


        tasks = self.load()



        for task in tasks:


            if task["id"] == task_id:


                task["status"] = "completed"


                task["finished"] = datetime.now().isoformat()



        self.save(
            tasks
        )




    def get_all_tasks(
        self
    ):


        return self.load()

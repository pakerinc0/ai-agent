from app.memory.database import Database


class MemoryManager:


    def __init__(self):

        self.db = Database()



    def search(
        self,
        task: str
    ):

        memories = self.db.search_memory(
            task
        )

        return memories



    def add(
        self,
        task: str,
        data: dict
    ):


        self.db.add_memory(

            task,

            str(data),

            "completed"

        )

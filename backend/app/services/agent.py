from datetime import datetime

from app.services.memory import Memory


class Agent:


    def __init__(self):

        self.name = "AI Agent"

        self.version = "0.1 beta"

        self.created_at = datetime.now()

        self.memory = Memory("user_1")



    async def process(self, message: str):

        response = (
            f"Я получил сообщение: {message}"
        )


        self.memory.save(
            message,
            response
        )


        return {

            "agent": self.name,

            "version": self.version,

            "message": message,

            "response": response,

            "history": self.memory.get_history(),

            "time": str(datetime.now())
        }

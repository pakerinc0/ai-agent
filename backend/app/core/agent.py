from app.ai.llm import LMStudioClient


class Agent:


    def __init__(self):

        self.llm = LMStudioClient()



    async def run(self, prompt: str):

        response = await self.llm.generate(
            prompt
        )

        return response

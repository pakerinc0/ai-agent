import httpx


class OllamaClient:

    def __init__(self):

        self.url = "http://192.168.100.111:11434/api/generate"
        self.model = "qwen3:8b"


    async def generate(self, prompt: str):

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }


        async with httpx.AsyncClient(timeout=120) as client:

            response = await client.post(
                self.url,
                json=payload
            )


        data = response.json()


        return data.get(
            "response",
            "Нет ответа от модели"
        )

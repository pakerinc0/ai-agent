import httpx
from typing import Optional

from app.ai.base import AIProvider



class LMStudioProvider(AIProvider):


    def __init__(self):

        self.base_url = "http://192.168.100.111:1234/v1/chat/completions"

        self.default_model = "eva-qwen2.5-7b-v0.0"



    async def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        **kwargs
    ) -> str:


        messages = []


        if system_prompt:

            messages.append(
                {
                    "role": "system",
                    "content": system_prompt
                }
            )


        messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )


        payload = {

            "model": kwargs.get(
                "model",
                self.default_model
            ),

            "messages": messages,

            "temperature": kwargs.get(
                "temperature",
                0.7
            ),

            "stream": False

        }



        try:


            async with httpx.AsyncClient(
                timeout=300
            ) as client:


                response = await client.post(
                    self.base_url,
                    json=payload
                )



            if response.status_code != 200:

                return (
                    f"LM Studio error: "
                    f"{response.status_code}\n"
                    f"{response.text}"
                )



            data = response.json()



            return data["choices"][0]["message"]["content"]



        except Exception as e:

            return (
                f"LM Studio connection error: {e}"
            )

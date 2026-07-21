import httpx



class LMStudioClient:


    def __init__(self):

        # IP компьютера с LM Studio
        self.url = "http://192.168.100.111:1234/v1/chat/completions"

        # модель из LM Studio
        self.model = "qwen3-8b"



    async def generate(self, prompt: str):


        data = {

            "model": self.model,

            "messages": [

                {
                    "role": "user",
                    "content": prompt
                }

            ],

            "temperature":0.7

        }



        try:

            async with httpx.AsyncClient(
                timeout=600
            ) as client:


                response = await client.post(
                    self.url,
                    json=data
                )



            result = response.json()



            return result["choices"][0]["message"]["content"]



        except Exception as e:


            print(
                "LM STUDIO ERROR:",
                e
            )


            return ""

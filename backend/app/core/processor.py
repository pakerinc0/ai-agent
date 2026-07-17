class Processor:


    def analyze(self, message: str):

        text = message.lower()


        # обычный разговор

        if any(word in text for word in [
            "привет",
            "hello",
            "здравствуй"
        ]):

            return {

                "type": "conversation",
                "intent": "greeting",
                "confidence": 0.9

            }



        # команды проверки системы

        if any(word in text for word in [
            "сервер",
            "система",
            "систему",
            "компьютер",
            "пк",
            "проверь",
            "проверить"
        ]):

            return {

                "type": "command",
                "intent": "system_check",
                "confidence": 0.8

            }



        return {

            "type": "conversation",
            "intent": "unknown",
            "confidence": 0.3

        }

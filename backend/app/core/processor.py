class Processor:


    def analyze(self, message: str):

        text = message.lower()


        # =========================
        # FILE / CODE TASKS
        # =========================

        if any(word in text for word in [
            "создай",
            "создать",
            "напиши",
            "сделай",
            "файл",
            "код",
            "python",
            ".py",
            "запусти",
            "запустить"
        ]):

            return {

                "type": "command",
                "intent": "file_task",
                "confidence": 0.95

            }



        # =========================
        # SYSTEM CHECK
        # =========================

        if any(word in text for word in [
            "сервер",
            "система",
            "компьютер",
            "пк",
            "проверь"
        ]):

            return {

                "type": "command",
                "intent": "system_check",
                "confidence": 0.8

            }



        # =========================
        # GREETING
        # =========================

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



        return {

            "type": "conversation",
            "intent": "unknown",
            "confidence": 0.3

        }

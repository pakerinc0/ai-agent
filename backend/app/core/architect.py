class Architect:


    def design(self, request: str):

        text = request.lower()


        # приложение с графикой

        if any(word in text for word in [
            "график",
            "визуал",
            "интерактив",
            "приложение",
            "игра"
        ]):

            return {

                "type": "application",

                "architecture": {

                    "frontend": [

                        "index.html",
                        "style.css",
                        "app.js"

                    ],

                    "backend": [

                        "main.py",
                        "logic.py"

                    ],

                    "docs": [

                        "README.md"

                    ]

                }

            }



        # обычный python проект

        return {


            "type": "python_project",

            "architecture": {


                "files": [

                    "main.py",
                    "README.md"

                ]

            }

        }

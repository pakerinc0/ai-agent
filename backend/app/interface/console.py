from app.core.orchestrator import Orchestrator


def main():

    print("=" * 50)
    print("AI Agent started")
    print("Введите задачу или 'exit' для выхода")
    print("=" * 50)


    agent = Orchestrator()


    while True:

        try:

            message = input("\n> ")


            if message.lower() in [
                "exit",
                "quit",
                "выход"
            ]:
                print("Agent stopped")
                break



            if not message.strip():
                continue



            result = agent.run(message)


            print("\n===== RESULT =====")


            for key, value in result.items():

                print(f"\n### {key}")
                print(value)



        except KeyboardInterrupt:

            print("\nAgent stopped")
            break



        except Exception as e:

            print("\nERROR:")
            print(e)



if __name__ == "__main__":

    main()

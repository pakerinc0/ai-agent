import json


def print_result(data):

    print("\n")
    print("=" * 70)
    print("🤖 AI AGENT RESULT")
    print("=" * 70)


    if "task" in data:

        print("\n📌 TASK:")
        print(data["task"])



    if "architecture" in data:

        print("\n🏗 ARCHITECTURE:")

        architecture = data["architecture"]


        if isinstance(architecture, dict):

            if "error" in architecture:

                print("\n❌ ERROR:")
                print(
                    architecture["error"]
                )


                if "raw" in architecture:

                    print("\nRAW:")
                    print(
                        architecture["raw"][:3000]
                    )


            else:

                print(
                    json.dumps(
                        architecture,
                        indent=4,
                        ensure_ascii=False
                    )
                )


        else:

            print(architecture)



    if "build" in data:

        print("\n🔨 BUILD:")

        print(
            json.dumps(
                data["build"],
                indent=4,
                ensure_ascii=False
            )
        )



    if "code" in data:

        print("\n💻 CODE:")

        print(
            json.dumps(
                data["code"],
                indent=4,
                ensure_ascii=False
            )
        )



    print("\n")
    print("=" * 70)
    print("✅ FINISHED")
    print("=" * 70)

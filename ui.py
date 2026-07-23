# Created by : Amarchand Meghwal
# AP AI Android v41.2

from engine.commands import execute
from engine.info import APP_NAME, VERSION, PROMPT, GOODBYE


def banner():
    print("\n" + "=" * 45)
    print(f"🤖 {APP_NAME} v{VERSION}")
    print("💬 Smart Assistant")
    print("=" * 45)
    print("Type 'bye' to exit.\n")


def start_app():
    banner()

    while True:
        try:
            message = input(PROMPT).strip()

            if not message:
                continue

            if message.lower() in ["bye", "exit", "quit"]:
                print(GOODBYE)
                break

            response = execute(message)

            if response is not None:
                print("AP AI :", response)

        except KeyboardInterrupt:
            print("\n" + GOODBYE)
            break

        except EOFError:
            print("\n" + GOODBYE)
            break

        except Exception as e:
            print(f"❌ Error: {e}")

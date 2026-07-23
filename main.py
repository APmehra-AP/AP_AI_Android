# Created by : Amarchand Meghwal
# AP AI Android v41

from ui import start_app
from engine.info import WELCOME, GOODBYE


def main():
    print(WELCOME)

    try:
        start_app()
    except KeyboardInterrupt:
        print("\n" + GOODBYE)


if __name__ == "__main__":
    main()

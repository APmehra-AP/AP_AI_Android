# Created by : Amarchand Meghwal

import json
import os

HISTORY_FILE = "history.json"

history_list = []


def load_history():
    global history_list

    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as f:
                history_list = json.load(f)
        except:
            history_list = []


def save_history():
    with open(HISTORY_FILE, "w") as f:
        json.dump(history_list, f, indent=4)


def add_history(command):
    command = command.strip()

    if command:
        history_list.append(command)

        # Sirf last 20 commands rakho
        if len(history_list) > 20:
            history_list.pop(0)

        save_history()


def show_history():
    if not history_list:
        return "📜 History is empty."

    result = "📜 Last Commands\n\n"

    for i, cmd in enumerate(history_list, 1):
        result += f"{i}. {cmd}\n"

    return result.strip()


def clear_history():
    history_list.clear()
    save_history()
    return "🗑 History cleared."


load_history()

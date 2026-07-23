# Created by : Amarchand Meghwal

import json
import os

SETTINGS_FILE = "settings.json"

settings = {
    "language": "Hindi",
    "theme": "Dark",
    "ai": "OpenRouter",
    "version": "34.0"
}


def load_settings():
    global settings

    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r") as f:
                settings = json.load(f)
        except:
            pass


def save_settings():
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)


def get_setting(key):
    return settings.get(key, "Not Found")


def set_setting(key, value):
    settings[key] = value
    save_settings()
    return f"✅ {key} updated to {value}"


def show_settings():
    result = "⚙ AP AI Settings\n\n"

    for key, value in settings.items():
        result += f"{key} : {value}\n"

    return result.strip()


load_settings()

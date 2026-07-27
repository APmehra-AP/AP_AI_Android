# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Application Settings Manager
"""

import json
import os

from engine.constants import SETTINGS_FILE


class SettingsManager:

    DEFAULT_SETTINGS = {
        "dark_mode": True,
        "voice_enabled": True,
        "voice_language": "hi-IN",
        "animations": True,
        "notifications": True,
        "remember_history": True,
        "remember_memory": True,
        "auto_scroll": True,
        "font_size": 16,
        "theme": "blue",
        "api_key": "",
        "model": "openai/gpt-5.5"
    }

    def __init__(self, filename=SETTINGS_FILE):
        self.filename = filename
        self.data = {}
        self.load()

    def load(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as file:
                    self.data = json.load(file)
            except Exception:
                self.data = self.DEFAULT_SETTINGS.copy()
        else:
            self.data = self.DEFAULT_SETTINGS.copy()
            self.save()

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(
                self.data,
                file,
                ensure_ascii=False,
                indent=4
            )

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value
        self.save()

    def update(self, values):
        if isinstance(values, dict):
            self.data.update(values)
            self.save()

    def reset(self):
        self.data = self.DEFAULT_SETTINGS.copy()
        self.save()

    def all(self):
        return dict(self.data)


settings = SettingsManager()

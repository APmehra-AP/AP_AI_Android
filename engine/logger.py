# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Application Logger
"""

import os
from datetime import datetime


class Logger:
    def __init__(self, filename="logs/app.log"):
        self.filename = filename
        folder = os.path.dirname(filename)

        if folder:
            os.makedirs(folder, exist_ok=True)

    def _write(self, level, message):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        line = f"[{now}] [{level}] {message}\n"

        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(line)

    def info(self, message):
        self._write("INFO", message)

    def warning(self, message):
        self._write("WARNING", message)

    def error(self, message):
        self._write("ERROR", message)

    def debug(self, message):
        self._write("DEBUG", message)

    def clear(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            file.write("")


logger = Logger()

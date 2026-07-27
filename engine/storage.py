# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Storage Helper
Handles reading and writing JSON files.
"""

import json
import os


class Storage:

    @staticmethod
    def load_json(filename, default=None):
        """Load JSON data from file."""

        if default is None:
            default = {}

        if not os.path.exists(filename):
            return default

        try:
            with open(filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception:
            return default

    @staticmethod
    def save_json(filename, data):
        """Save JSON data to file."""

        folder = os.path.dirname(filename)

        if folder:
            os.makedirs(folder, exist_ok=True)

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )

    @staticmethod
    def read_text(filename, default=""):
        """Read text file."""

        if not os.path.exists(filename):
            return default

        try:
            with open(filename, "r", encoding="utf-8") as file:
                return file.read()
        except Exception:
            return default

    @staticmethod
    def write_text(filename, text):
        """Write text file."""

        folder = os.path.dirname(filename)

        if folder:
            os.makedirs(folder, exist_ok=True)

        with open(filename, "w", encoding="utf-8") as file:
            file.write(str(text))

    @staticmethod
    def exists(filename):
        """Check whether file exists."""

        return os.path.exists(filename)

    @staticmethod
    def delete(filename):
        """Delete file if it exists."""

        if os.path.exists(filename):
            os.remove(filename)
            return True

        return False

    @staticmethod
    def file_size(filename):
        """Return file size in bytes."""

        if os.path.exists(filename):
            return os.path.getsize(filename)

        return 0

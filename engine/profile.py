# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
User Profile Manager
"""

import json
import os


class ProfileManager:

    def __init__(self, filename="profile.json"):
        self.filename = filename
        self.profile = {}
        self.load()

    def load(self):
        """
        Load profile from disk.
        """

        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as file:
                    self.profile = json.load(file)
            except Exception:
                self.profile = {}

    def save(self):
        """
        Save profile to disk.
        """

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(
                self.profile,
                file,
                ensure_ascii=False,
                indent=4
            )

    def set(self, key, value):
        """
        Set profile value.
        """

        self.profile[str(key)] = value
        self.save()

    def get(self, key, default=None):
        """
        Get profile value.
        """

        return self.profile.get(str(key), default)

    def update(self, values):
        """
        Update multiple values.
        """

        if isinstance(values, dict):
            self.profile.update(values)
            self.save()

    def remove(self, key):
        """
        Remove profile key.
        """

        if str(key) in self.profile:
            del self.profile[str(key)]
            self.save()
            return True

        return False

    def exists(self, key):
        """
        Check if profile key exists.
        """

        return str(key) in self.profile

    def all(self):
        """
        Return complete profile.
        """

        return dict(self.profile)

    def clear(self):
        """
        Clear profile.
        """

        self.profile.clear()
        self.save()


profile = ProfileManager()

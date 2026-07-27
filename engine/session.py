# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Session Manager
Stores runtime data while the app is running.
"""

from datetime import datetime


class SessionManager:
    def __init__(self):
        self.reset()

    def reset(self):
        """
        Reset session data.
        """

        self.started_at = datetime.now()

        self.data = {}

        self.state = "idle"

        self.current_screen = "home"

        self.user_message = ""

        self.ai_response = ""

    def set(self, key, value):
        """
        Store session value.
        """

        self.data[str(key)] = value

    def get(self, key, default=None):
        """
        Get session value.
        """

        return self.data.get(str(key), default)

    def remove(self, key):
        """
        Remove session value.
        """

        self.data.pop(str(key), None)

    def clear(self):
        """
        Clear session values.
        """

        self.data.clear()

    def set_state(self, state):
        """
        Update current app state.
        """

        self.state = str(state)

    def get_state(self):
        """
        Return current app state.
        """

        return self.state

    def set_screen(self, screen):
        """
        Update current screen.
        """

        self.current_screen = str(screen)

    def get_screen(self):
        """
        Return current screen.
        """

        return self.current_screen

    def uptime(self):
        """
        Return session uptime in seconds.
        """

        return int(
            (datetime.now() - self.started_at).total_seconds()
        )

    def summary(self):
        """
        Return session information.
        """

        return {
            "state": self.state,
            "screen": self.current_screen,
            "uptime": self.uptime(),
            "items": len(self.data)
        }


session = SessionManager()

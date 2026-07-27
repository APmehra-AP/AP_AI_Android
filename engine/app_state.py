# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Application State Manager
"""

from engine.constants import (
    STATUS_IDLE,
    STATUS_LISTENING,
    STATUS_THINKING,
    STATUS_SPEAKING,
    STATUS_ERROR,
)


class AppState:

    def __init__(self):
        self.reset()

    def reset(self):
        """
        Reset application state.
        """

        self.status = STATUS_IDLE
        self.online = False
        self.loading = False
        self.current_screen = "home"
        self.last_error = ""

    # --------------------------------------------------
    # Status
    # --------------------------------------------------

    def set_status(self, status):
        self.status = str(status)

    def get_status(self):
        return self.status

    def idle(self):
        self.status = STATUS_IDLE

    def listening(self):
        self.status = STATUS_LISTENING

    def thinking(self):
        self.status = STATUS_THINKING

    def speaking(self):
        self.status = STATUS_SPEAKING

    def error(self, message=""):
        self.status = STATUS_ERROR
        self.last_error = str(message)

    # --------------------------------------------------
    # Network
    # --------------------------------------------------

    def set_online(self, value):
        self.online = bool(value)

    def is_online(self):
        return self.online

    # --------------------------------------------------
    # Loading
    # --------------------------------------------------

    def set_loading(self, value):
        self.loading = bool(value)

    def is_loading(self):
        return self.loading

    # --------------------------------------------------
    # Screen
    # --------------------------------------------------

    def set_screen(self, name):
        self.current_screen = str(name)

    def get_screen(self):
        return self.current_screen

    # --------------------------------------------------
    # Error
    # --------------------------------------------------

    def get_last_error(self):
        return self.last_error

    # --------------------------------------------------
    # Summary
    # --------------------------------------------------

    def summary(self):
        return {
            "status": self.status,
            "online": self.online,
            "loading": self.loading,
            "screen": self.current_screen,
            "last_error": self.last_error,
        }


app_state = AppState()

# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Reusable Snackbar Manager
"""

from kivymd.uix.snackbar import (
    MDSnackbar,
    MDSnackbarText,
)


class SnackbarManager:
    """
    Simple reusable Snackbar helper.
    """

    @staticmethod
    def _show(message, duration=3):
        snackbar = MDSnackbar(
            MDSnackbarText(
                text=str(message)
            ),
            duration=duration,
        )

        snackbar.open()
        return snackbar

    @classmethod
    def info(cls, message, duration=3):
        return cls._show(message, duration)

    @classmethod
    def success(cls, message, duration=3):
        return cls._show(f"✓ {message}", duration)

    @classmethod
    def warning(cls, message, duration=3):
        return cls._show(f"⚠ {message}", duration)

    @classmethod
    def error(cls, message, duration=4):
        return cls._show(f"✖ {message}", duration)

    @classmethod
    def loading(cls, message="Loading...", duration=2):
        return cls._show(message, duration)


snackbar = SnackbarManager()

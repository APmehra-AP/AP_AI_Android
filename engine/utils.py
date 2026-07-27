# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Common utility functions used across AP AI.
"""

from datetime import datetime


def current_time():
    """Return current time in HH:MM format."""
    return datetime.now().strftime("%H:%M")


def current_date():
    """Return current date."""
    return datetime.now().strftime("%d-%m-%Y")


def current_datetime():
    """Return current date and time."""
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def greeting():
    """Return greeting according to current time."""

    hour = datetime.now().hour

    if hour < 12:
        return "Good Morning"

    if hour < 17:
        return "Good Afternoon"

    if hour < 21:
        return "Good Evening"

    return "Good Night"


def safe_text(value):
    """Convert any value to safe string."""

    if value is None:
        return ""

    return str(value).strip()


def is_blank(value):
    """Check if text is empty."""

    return safe_text(value) == ""


def app_title():
    from engine.config import APP_TITLE, VERSION

    return f"{APP_TITLE} {VERSION}"

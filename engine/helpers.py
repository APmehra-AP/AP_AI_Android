# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Common helper functions.
"""

import re
from datetime import datetime


def clean_text(text):
    """Return cleaned text."""

    if text is None:
        return ""

    text = str(text).strip()
    text = re.sub(r"\s+", " ", text)

    return text


def is_empty(text):
    """Check if text is empty."""

    return clean_text(text) == ""


def truncate(text, length=100):
    """Shorten text safely."""

    text = clean_text(text)

    if len(text) <= length:
        return text

    return text[:length - 3] + "..."


def timestamp():
    """Current timestamp."""

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def yes(value):
    """Return True for common yes values."""

    return clean_text(value).lower() in {
        "yes",
        "y",
        "true",
        "1",
        "haan",
        "ha",
        "han"
    }


def no(value):
    """Return True for common no values."""

    return clean_text(value).lower() in {
        "no",
        "n",
        "false",
        "0",
        "nahi",
        "nahin"
    }


def safe_int(value, default=0):
    """Convert to integer safely."""

    try:
        return int(value)
    except (ValueError, TypeError):
        return default


def safe_float(value, default=0.0):
    """Convert to float safely."""

    try:
        return float(value)
    except (ValueError, TypeError):
        return default


def clamp(value, minimum, maximum):
    """Clamp value within range."""

    return max(minimum, min(value, maximum))


def unique(items):
    """Return unique items preserving order."""

    seen = set()
    result = []

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result

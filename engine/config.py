# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Global Configuration

This file contains application configuration.
Do not hardcode secrets here.
"""

from engine.theme import APP_NAME, APP_VERSION

# ---------------------------------------------------------
# APP
# ---------------------------------------------------------

APP_TITLE = APP_NAME
VERSION = APP_VERSION

# ---------------------------------------------------------
# AI
# ---------------------------------------------------------

AI_NAME = "AP AI"

DEFAULT_MODEL = "openai/gpt-5.5"

SYSTEM_PROMPT = (
    "You are AP AI, created by Amarchand Meghwal. "
    "Reply in the same language as the user. "
    "Be accurate, friendly, concise, and helpful."
)

# ---------------------------------------------------------
# API
# ---------------------------------------------------------

OPENROUTER_API_KEY = ""

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

REQUEST_TIMEOUT = 60

# ---------------------------------------------------------
# CHAT
# ---------------------------------------------------------

MAX_HISTORY = 20

MAX_MEMORY = 500

# ---------------------------------------------------------
# VOICE
# ---------------------------------------------------------

VOICE_ENABLED = True

VOICE_LANGUAGE = "hi-IN"

# ---------------------------------------------------------
# SETTINGS
# ---------------------------------------------------------

DARK_MODE = True

ENABLE_ANIMATIONS = True

ENABLE_MEMORY = True

ENABLE_LOGS = True

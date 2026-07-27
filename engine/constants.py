# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Application Constants
"""

# ---------------------------------------------------------
# APP
# ---------------------------------------------------------

APP_AUTHOR = "Amarchand Meghwal"
APP_COPYRIGHT = "© AP AI"

# ---------------------------------------------------------
# CHAT
# ---------------------------------------------------------

ROLE_SYSTEM = "system"
ROLE_USER = "user"
ROLE_ASSISTANT = "assistant"

# ---------------------------------------------------------
# STATUS
# ---------------------------------------------------------

STATUS_IDLE = "idle"
STATUS_LISTENING = "listening"
STATUS_THINKING = "thinking"
STATUS_SPEAKING = "speaking"
STATUS_ERROR = "error"

# ---------------------------------------------------------
# EVENTS
# ---------------------------------------------------------

EVENT_APP_START = "app_start"
EVENT_APP_CLOSE = "app_close"

EVENT_CHAT_SEND = "chat_send"
EVENT_CHAT_REPLY = "chat_reply"

EVENT_MEMORY_CHANGED = "memory_changed"

EVENT_THEME_CHANGED = "theme_changed"

EVENT_VOICE_START = "voice_start"
EVENT_VOICE_STOP = "voice_stop"

# ---------------------------------------------------------
# FILES
# ---------------------------------------------------------

MEMORY_FILE = "memory.json"
SETTINGS_FILE = "settings.json"
HISTORY_FILE = "history.json"

LOG_DIR = "logs"
LOG_FILE = "logs/app.log"

CACHE_DIR = "cache"

# ---------------------------------------------------------
# NETWORK
# ---------------------------------------------------------

DEFAULT_TIMEOUT = 60

# ---------------------------------------------------------
# UI
# ---------------------------------------------------------

ANIMATION_FAST = 0.15
ANIMATION_NORMAL = 0.30
ANIMATION_SLOW = 0.50

DEFAULT_PADDING = 16
DEFAULT_RADIUS = 18
DEFAULT_SPACING = 10

# ---------------------------------------------------------
# VOICE
# ---------------------------------------------------------

VOICE_LANGUAGE = "hi-IN"

# ---------------------------------------------------------
# DEFAULT MESSAGES
# ---------------------------------------------------------

WELCOME_MESSAGE = (
    "नमस्ते! मैं AP AI हूँ। आपकी सहायता के लिए तैयार हूँ।"
)

ERROR_MESSAGE = (
    "माफ़ कीजिए, अनुरोध पूरा नहीं हो सका।"
)

NO_INTERNET_MESSAGE = (
    "इंटरनेट कनेक्शन उपलब्ध नहीं है।"
)

LOADING_MESSAGE = "सोच रहा हूँ..."

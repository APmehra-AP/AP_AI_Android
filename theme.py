# Created by : Amarchand Meghwal

from kivy.metrics import dp


class Theme:
    # App
    APP_NAME = "AP AI"
    VERSION = "2.0"

    # Background
    BG = (0.04, 0.05, 0.09, 1)
    SURFACE = (0.09, 0.11, 0.17, 1)
    CARD = (0.12, 0.15, 0.23, 1)

    # Primary Colours
    PRIMARY = (0.00, 0.72, 1.00, 1)
    PRIMARY_DARK = (0.00, 0.52, 0.85, 1)
    ACCENT = (0.10, 0.85, 1.00, 1)

    # Text
    TEXT = (1, 1, 1, 1)
    TEXT_SECONDARY = (0.72, 0.78, 0.88, 1)

    # Status
    SUCCESS = (0.20, 0.80, 0.45, 1)
    WARNING = (1.00, 0.72, 0.10, 1)
    ERROR = (1.00, 0.25, 0.25, 1)

    # Layout
    PADDING = dp(20)
    SPACING = dp(15)
    RADIUS = dp(20)

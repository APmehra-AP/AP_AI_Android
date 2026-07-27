# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Reusable GUI Widgets
"""

from kivy.metrics import dp
from kivy.utils import get_color_from_hex

from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField

from gui.theme import (
    PRIMARY,
    CARD,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
    RADIUS,
)


class APCard(MDCard):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.radius = [RADIUS]
        self.padding = dp(16)
        self.spacing = dp(10)
        self.md_bg_color = get_color_from_hex(CARD)


class APLabel(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.theme_text_color = "Custom"
        self.text_color = get_color_from_hex(TEXT_PRIMARY)


class APSecondaryLabel(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.theme_text_color = "Custom"
        self.text_color = get_color_from_hex(TEXT_SECONDARY)


class APTextField(MDTextField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.mode = "outlined"
        self.size_hint_y = None
        self.height = dp(56)


class APButton(MDButton):
    def __init__(self, text="", **kwargs):
        super().__init__(**kwargs)

        self.style = "filled"
        self.md_bg_color = get_color_from_hex(PRIMARY)

        self.add_widget(
            MDButtonText(
                text=text
            )
        )

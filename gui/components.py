# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Reusable GUI Components
"""

from kivy.metrics import dp
from kivy.utils import get_color_from_hex
from kivy.clock import Clock

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.progressindicator import MDCircularProgressIndicator

from gui.theme import (
    PRIMARY,
    CARD,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
    RADIUS
)


class HeaderBar(MDBoxLayout):
    """
    Top header component.
    """

    def __init__(self, title="AP AI", **kwargs):
        super().__init__(**kwargs)

        self.orientation = "horizontal"
        self.adaptive_height = True
        self.padding = dp(16)
        self.spacing = dp(10)

        self.add_widget(
            MDLabel(
                text=title,
                bold=True,
                font_style="Headline",
                theme_text_color="Custom",
                text_color=get_color_from_hex(TEXT_PRIMARY)
            )
        )


class ChatBubble(MDBoxLayout):
    """
    Chat message bubble.
    """

    def __init__(self, message="", sender="assistant", **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.adaptive_height = True
        self.padding = dp(12)
        self.spacing = dp(6)

        if sender == "user":
            bg = PRIMARY
        else:
            bg = CARD

        self.md_bg_color = get_color_from_hex(bg)
        self.radius = [RADIUS]

        self.add_widget(
            MDLabel(
                text=message,
                adaptive_height=True,
                theme_text_color="Custom",
                text_color=get_color_from_hex(TEXT_PRIMARY)
            )
        )


class LoadingIndicator(MDBoxLayout):
    """
    Thinking animation.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "horizontal"
        self.adaptive_height = True
        self.spacing = dp(10)

        self.spinner = MDCircularProgressIndicator(
            size_hint=(None, None),
            size=(dp(26), dp(26))
        )

        self.label = MDLabel(
            text="Thinking...",
            adaptive_height=True,
            theme_text_color="Custom",
            text_color=get_color_from_hex(TEXT_SECONDARY)
        )

        self.add_widget(self.spinner)
        self.add_widget(self.label)


class StatusBar(MDBoxLayout):
    """
    Bottom status bar.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "horizontal"
        self.adaptive_height = True
        self.padding = dp(10)

        self.label = MDLabel(
            text="Ready",
            adaptive_height=True,
            theme_text_color="Custom",
            text_color=get_color_from_hex(TEXT_SECONDARY)
        )

        self.add_widget(self.label)

    def set_status(self, text):
        self.label.text = str(text)


class ToastMessage(MDLabel):
    """
    Temporary message widget.
    """

    def __init__(self, text="", duration=2, **kwargs):
        super().__init__(**kwargs)

        self.text = text
        self.opacity = 1
        self.halign = "center"
        self.theme_text_color = "Custom"
        self.text_color = get_color_from_hex(TEXT_PRIMARY)

        Clock.schedule_once(
            self.dismiss,
            duration
        )

    def dismiss(self, *_):
        self.opacity = 0

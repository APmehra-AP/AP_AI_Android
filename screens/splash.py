# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Splash Screen
"""

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.utils import get_color_from_hex

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

from gui.theme import (
    BACKGROUND,
    PRIMARY,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
)


class SplashScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name = "splash"

        self.md_bg_color = get_color_from_hex(
            BACKGROUND
        )

        root = MDBoxLayout(
            orientation="vertical",
            spacing=dp(20),
            padding=dp(30)
        )

        root.add_widget(MDBoxLayout())

        self.logo = MDLabel(
            text="AP",
            halign="center",
            theme_text_color="Custom",
            text_color=get_color_from_hex(PRIMARY),
            font_style="Display",
            opacity=0
        )

        root.add_widget(self.logo)

        self.title = MDLabel(
            text="AP AI",
            halign="center",
            theme_text_color="Custom",
            text_color=get_color_from_hex(TEXT_PRIMARY),
            font_style="Headline",
            opacity=0
        )

        root.add_widget(self.title)

        self.subtitle = MDLabel(
            text="Your Personal AI Assistant",
            halign="center",
            theme_text_color="Custom",
            text_color=get_color_from_hex(TEXT_SECONDARY),
            opacity=0
        )

        root.add_widget(self.subtitle)

        root.add_widget(MDBoxLayout())

        self.add_widget(root)

    def on_enter(self, *args):

        Animation(
            opacity=1,
            duration=0.8
        ).start(self.logo)

        Animation(
            opacity=1,
            duration=1.0
        ).start(self.title)

        Animation(
            opacity=1,
            duration=1.2
        ).start(self.subtitle)

        Clock.schedule_once(
            self.goto_home,
            2.5
        )

    def goto_home(self, *_):

        return

# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Settings Screen
"""

from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout

from gui.components import HeaderBar, StatusBar
from gui.widgets import (
    APCard,
    APButton,
    APLabel,
    APTextField
)

from engine.settings import settings


class SettingsScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name = "settings"

        root = MDBoxLayout(
            orientation="vertical",
            spacing="10dp",
            padding="10dp"
        )

        # ---------------------------------
        # Header
        # ---------------------------------

        root.add_widget(
            HeaderBar("Settings")
        )

        # ---------------------------------
        # Card
        # ---------------------------------

        card = APCard(
            orientation="vertical"
        )

        card.add_widget(
            APLabel(
                text="OpenRouter API Key"
            )
        )

        self.api_key = APTextField(
            hint_text="Paste API Key"
        )

        self.api_key.text = settings.get(
            "api_key",
            ""
        )

        card.add_widget(self.api_key)

        card.add_widget(
            APLabel(
                text="AI Model"
            )
        )

        self.model = APTextField(
            hint_text="Model"
        )

        self.model.text = settings.get(
            "model",
            "openai/gpt-5.5"
        )

        card.add_widget(self.model)

        self.save_button = APButton(
            text="Save Settings"
        )

        self.save_button.bind(
            on_release=self.save_settings
        )

        card.add_widget(
            self.save_button
        )

        root.add_widget(card)

        # ---------------------------------
        # Status
        # ---------------------------------

        self.status = StatusBar()

        root.add_widget(
            self.status
        )

        self.add_widget(root)

    # -------------------------------------

    def save_settings(self, *_):

        settings.set(
            "api_key",
            self.api_key.text.strip()
        )

        settings.set(
            "model",
            self.model.text.strip()
        )

        self.status.set_status(
            "Settings Saved"
        )

    # -------------------------------------

    def load_settings(self):

        self.api_key.text = settings.get(
            "api_key",
            ""
        )

        self.model.text = settings.get(
            "model",
            "openai/gpt-5.5"
        )

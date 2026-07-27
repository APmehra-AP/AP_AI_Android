# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Profile Screen
"""

from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout

from gui.components import HeaderBar, StatusBar
from gui.widgets import (
    APCard,
    APLabel,
    APButton,
    APTextField,
)

from engine.profile import profile


class ProfileScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name = "profile"

        root = MDBoxLayout(
            orientation="vertical",
            spacing="10dp",
            padding="10dp"
        )

        root.add_widget(
            HeaderBar("Profile")
        )

        card = APCard(
            orientation="vertical"
        )

        card.add_widget(
            APLabel(
                text="Name"
            )
        )

        self.name_field = APTextField(
            hint_text="Your Name"
        )

        card.add_widget(
            self.name_field
        )

        card.add_widget(
            APLabel(
                text="Email"
            )
        )

        self.email_field = APTextField(
            hint_text="Email"
        )

        card.add_widget(
            self.email_field
        )

        card.add_widget(
            APLabel(
                text="Language"
            )
        )

        self.language_field = APTextField(
            hint_text="hi"
        )

        card.add_widget(
            self.language_field
        )

        self.save_button = APButton(
            text="Save Profile"
        )

        self.save_button.bind(
            on_release=self.save_profile
        )

        card.add_widget(
            self.save_button
        )

        root.add_widget(card)

        self.status = StatusBar()

        root.add_widget(
            self.status
        )

        self.add_widget(root)

        self.load_profile()

    def load_profile(self):

        self.name_field.text = profile.get(
            "name",
            ""
        )

        self.email_field.text = profile.get(
            "email",
            ""
        )

        self.language_field.text = profile.get(
            "language",
            "hi"
        )

    def save_profile(self, *_):

        profile.set(
            "name",
            self.name_field.text.strip()
        )

        profile.set(
            "email",
            self.email_field.text.strip()
        )

        profile.set(
            "language",
            self.language_field.text.strip()
        )

        self.status.set_status(
            "Profile Saved"
        )

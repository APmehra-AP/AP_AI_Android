# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
About Screen
"""

from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout

from gui.components import HeaderBar, StatusBar
from gui.widgets import APCard, APLabel


class AboutScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name = "about"

        root = MDBoxLayout(
            orientation="vertical",
            spacing="10dp",
            padding="10dp"
        )

        # Header
        root.add_widget(
            HeaderBar("About AP AI")
        )

        # About Card
        card = APCard(
            orientation="vertical"
        )

        card.add_widget(
            APLabel(
                text="AP AI V4 Stable"
            )
        )

        card.add_widget(
            APLabel(
                text="Developer: Amarchand Meghwal"
            )
        )

        card.add_widget(
            APLabel(
                text="Version: 4.0 Stable"
            )
        )

        card.add_widget(
            APLabel(
                text=(
                    "AP AI is a personal AI assistant "
                    "designed to provide intelligent "
                    "chat, voice interaction, memory "
                    "management and productivity tools."
                )
            )
        )

        root.add_widget(card)

        # Status Bar
        self.status = StatusBar()
        self.status.set_status("Ready")

        root.add_widget(self.status)

        self.add_widget(root)

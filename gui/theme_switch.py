# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Theme Switch Widget
"""

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.selectioncontrol import MDSwitch


class ThemeSwitch(MDBoxLayout):
    """
    Reusable Light/Dark Theme Switch
    """

    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)

        self.app = app

        self.orientation = "horizontal"
        self.spacing = "12dp"
        self.adaptive_height = True

        self.label = MDLabel(
            text="Dark Theme",
            adaptive_height=True,
            valign="center"
        )

        self.switch = MDSwitch()

        if self.app:
            self.switch.active = (
                self.app.theme_cls.theme_style == "Dark"
            )

        self.switch.bind(active=self.on_switch)

        self.add_widget(self.label)
        self.add_widget(self.switch)

    def on_switch(self, instance, value):

        if not self.app:
            return

        if value:
            self.app.theme_cls.theme_style = "Dark"
        else:
            self.app.theme_cls.theme_style = "Light"

    def set_theme(self, theme):

        if not self.app:
            return

        if theme not in ("Light", "Dark"):
            return

        self.app.theme_cls.theme_style = theme
        self.switch.active = (theme == "Dark")

    def get_theme(self):

        if not self.app:
            return "Dark"

        return self.app.theme_cls.theme_style

    def toggle(self):

        self.switch.active = not self.switch.active

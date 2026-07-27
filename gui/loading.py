# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Reusable Loading Components
"""

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivy.metrics import dp


class LoadingWidget(MDBoxLayout):
    """
    Small loading spinner with text.
    """

    def __init__(self, text="Loading...", **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.spacing = dp(10)
        self.padding = dp(20)
        self.adaptive_height = True
        self.adaptive_width = True
        self.pos_hint = {
            "center_x": 0.5,
            "center_y": 0.5
        }

        self.spinner = MDSpinner(
            size_hint=(None, None),
            size=(dp(46), dp(46)),
            active=True
        )

        self.label = MDLabel(
            text=text,
            halign="center",
            adaptive_height=True
        )

        self.add_widget(self.spinner)
        self.add_widget(self.label)

    def start(self):
        self.spinner.active = True

    def stop(self):
        self.spinner.active = False

    def set_text(self, text):
        self.label.text = text


class LoadingOverlay(MDCard):
    """
    Full-screen loading overlay.
    """

    def __init__(self, text="Please wait...", **kwargs):
        super().__init__(**kwargs)

        self.size_hint = (1, 1)
        self.elevation = 0
        self.radius = [0, 0, 0, 0]
        self.opacity = 0
        self.disabled = True

        container = MDBoxLayout(
            orientation="vertical",
            adaptive_size=True,
            spacing=dp(15),
            pos_hint={
                "center_x": 0.5,
                "center_y": 0.5
            }
        )

        self.loader = LoadingWidget(text)

        container.add_widget(self.loader)
        self.add_widget(container)

    def show(self, text=None):
        if text:
            self.loader.set_text(text)

        self.loader.start()
        self.opacity = 1
        self.disabled = False

    def hide(self):
        self.loader.stop()
        self.opacity = 0
        self.disabled = True

    @property
    def visible(self):
        return not self.disabled

# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Reusable Search Bar
"""

from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton


class APSearchBar(MDBoxLayout):
    """
    Reusable Search Bar Widget
    """

    def __init__(
        self,
        hint="Search...",
        callback=None,
        **kwargs
    ):
        super().__init__(**kwargs)

        self.orientation = "horizontal"
        self.adaptive_height = True
        self.spacing = "8dp"

        self.callback = callback

        self.search_field = MDTextField(
            hint_text=hint,
            mode="outlined"
        )

        self.search_button = MDIconButton(
            icon="magnify"
        )

        self.clear_button = MDIconButton(
            icon="close"
        )

        self.search_button.bind(
            on_release=self.search
        )

        self.clear_button.bind(
            on_release=self.clear
        )

        self.search_field.bind(
            on_text_validate=self.search
        )

        self.add_widget(self.search_field)
        self.add_widget(self.search_button)
        self.add_widget(self.clear_button)

    # --------------------------------------------------

    def search(self, *args):

        text = self.search_field.text.strip()

        if callable(self.callback):
            self.callback(text)

    # --------------------------------------------------

    def clear(self, *args):

        self.search_field.text = ""

    # --------------------------------------------------

    def get_text(self):

        return self.search_field.text.strip()

    # --------------------------------------------------

    def set_text(self, text):

        self.search_field.text = str(text)

    # --------------------------------------------------

    def set_hint(self, hint):

        self.search_field.hint_text = hint

    # --------------------------------------------------

    def focus(self):

        self.search_field.focus = True

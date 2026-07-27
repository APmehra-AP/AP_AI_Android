# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Reusable File Picker
"""

import os

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import (
    MDList,
    MDListItem,
    MDListItemHeadlineText,
)
from kivymd.uix.scrollview import MDScrollView


class FilePicker(MDBoxLayout):
    """
    Simple reusable file picker.
    """

    def __init__(
        self,
        start_path=".",
        select_callback=None,
        **kwargs
    ):
        super().__init__(**kwargs)

        self.orientation = "vertical"

        self.current_path = os.path.abspath(start_path)
        self.select_callback = select_callback

        self.scroll = MDScrollView()

        self.list_view = MDList()

        self.scroll.add_widget(self.list_view)
        self.add_widget(self.scroll)

        self.load_directory(self.current_path)

    # --------------------------------------------------

    def load_directory(self, path):

        self.current_path = os.path.abspath(path)

        self.list_view.clear_widgets()

        # Parent directory
        parent = os.path.dirname(self.current_path)

        if parent != self.current_path:

            item = MDListItem()

            item.add_widget(
                MDListItemHeadlineText(
                    text=".."
                )
            )

            item.bind(
                on_release=lambda *_: self.load_directory(parent)
            )

            self.list_view.add_widget(item)

        try:
            entries = sorted(os.listdir(self.current_path))

        except Exception:
            entries = []

        for name in entries:

            full_path = os.path.join(
                self.current_path,
                name
            )

            item = MDListItem()

            prefix = "📁 " if os.path.isdir(full_path) else "📄 "

            item.add_widget(
                MDListItemHeadlineText(
                    text=prefix + name
                )
            )

            if os.path.isdir(full_path):

                item.bind(
                    on_release=lambda _, p=full_path: self.load_directory(p)
                )

            else:

                item.bind(
                    on_release=lambda _, p=full_path: self.select_file(p)
                )

            self.list_view.add_widget(item)

    # --------------------------------------------------

    def select_file(self, path):

        if callable(self.select_callback):
            self.select_callback(path)

    # --------------------------------------------------

    def refresh(self):

        self.load_directory(self.current_path)

    # --------------------------------------------------

    def get_current_path(self):

        return self.current_path

    # --------------------------------------------------

    def set_callback(self, callback):

        self.select_callback = callback

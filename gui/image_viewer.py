# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Reusable Image Viewer
"""

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivy.uix.image import Image


class ImageViewer(MDBoxLayout):
    """
    Reusable image viewer.
    """

    def __init__(self, image_path="", **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.spacing = "8dp"

        self.scale = 1.0

        self.image = Image(
            source=image_path,
            allow_stretch=True,
            keep_ratio=True
        )

        self.toolbar = MDBoxLayout(
            adaptive_height=True,
            spacing="4dp"
        )

        self.zoom_in_btn = MDIconButton(
            icon="magnify-plus"
        )

        self.zoom_out_btn = MDIconButton(
            icon="magnify-minus"
        )

        self.fit_btn = MDIconButton(
            icon="fit-to-page"
        )

        self.reload_btn = MDIconButton(
            icon="reload"
        )

        self.zoom_in_btn.bind(
            on_release=self.zoom_in
        )

        self.zoom_out_btn.bind(
            on_release=self.zoom_out
        )

        self.fit_btn.bind(
            on_release=self.fit_image
        )

        self.reload_btn.bind(
            on_release=self.reload
        )

        self.toolbar.add_widget(self.zoom_in_btn)
        self.toolbar.add_widget(self.zoom_out_btn)
        self.toolbar.add_widget(self.fit_btn)
        self.toolbar.add_widget(self.reload_btn)

        self.add_widget(self.toolbar)
        self.add_widget(self.image)

    # --------------------------------------------------

    def set_image(self, path):
        self.image.source = path
        self.image.reload()

    # --------------------------------------------------

    def reload(self, *args):
        self.image.reload()

    # --------------------------------------------------

    def zoom_in(self, *args):
        self.scale += 0.1
        self._apply_scale()

    # --------------------------------------------------

    def zoom_out(self, *args):
        self.scale = max(0.2, self.scale - 0.1)
        self._apply_scale()

    # --------------------------------------------------

    def fit_image(self, *args):
        self.scale = 1.0
        self._apply_scale()

    # --------------------------------------------------

    def _apply_scale(self):
        self.image.size_hint = (
            self.scale,
            self.scale
        )

    # --------------------------------------------------

    def current_image(self):
        return self.image.source

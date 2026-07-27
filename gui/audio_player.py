# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Reusable Audio Player
"""

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.slider import MDSlider
from kivymd.uix.label import MDLabel

from kivy.core.audio import SoundLoader
from kivy.clock import Clock


class AudioPlayer(MDBoxLayout):
    """
    Simple reusable audio player.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.spacing = "8dp"

        self.sound = None
        self.duration = 0

        self.info = MDLabel(
            text="No audio loaded",
            halign="center",
            adaptive_height=True
        )

        self.progress = MDSlider(
            min=0,
            max=100,
            value=0
        )

        self.controls = MDBoxLayout(
            adaptive_height=True,
            spacing="8dp"
        )

        self.play_btn = MDIconButton(icon="play")
        self.pause_btn = MDIconButton(icon="pause")
        self.stop_btn = MDIconButton(icon="stop")

        self.play_btn.bind(on_release=self.play)
        self.pause_btn.bind(on_release=self.pause)
        self.stop_btn.bind(on_release=self.stop)

        self.progress.bind(value=self.seek)

        self.controls.add_widget(self.play_btn)
        self.controls.add_widget(self.pause_btn)
        self.controls.add_widget(self.stop_btn)

        self.add_widget(self.info)
        self.add_widget(self.progress)
        self.add_widget(self.controls)

        Clock.schedule_interval(self.update_progress, 0.5)

    # -------------------------------------------------

    def load(self, path):

        self.stop()

        self.sound = SoundLoader.load(path)

        if self.sound:
            self.info.text = path.split("/")[-1]
            self.duration = self.sound.length or 0
            self.progress.max = max(1, self.duration)
            self.progress.value = 0
            return True

        self.info.text = "Failed to load audio"
        return False

    # -------------------------------------------------

    def play(self, *args):

        if self.sound:
            self.sound.play()

    # -------------------------------------------------

    def pause(self, *args):

        if self.sound:
            self.sound.stop()

    # -------------------------------------------------

    def stop(self, *args):

        if self.sound:
            self.sound.stop()

        self.progress.value = 0

    # -------------------------------------------------

    def seek(self, instance, value):

        if self.sound and self.duration > 0:
            try:
                self.sound.seek(value)
            except Exception:
                pass

    # -------------------------------------------------

    def update_progress(self, dt):

        if self.sound and self.sound.state == "play":

            try:
                pos = self.sound.get_pos()

                if pos >= 0:
                    self.progress.value = pos

            except Exception:
                pass

    # -------------------------------------------------

    def is_loaded(self):

        return self.sound is not None

    # -------------------------------------------------

    def unload(self):

        self.stop()

        self.sound = None
        self.duration = 0
        self.info.text = "No audio loaded"
        self.progress.value = 0

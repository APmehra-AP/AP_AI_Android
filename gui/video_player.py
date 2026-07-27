# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Reusable Video Player
"""

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.slider import MDSlider

from kivy.uix.video import Video
from kivy.clock import Clock


class VideoPlayer(MDBoxLayout):
    """
    Reusable video player widget.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.spacing = "8dp"

        self.video = Video(
            state="stop",
            options={"eos": "stop"}
        )

        self.info = MDLabel(
            text="No video loaded",
            halign="center",
            adaptive_height=True
        )

        self.slider = MDSlider(
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
        self.reload_btn = MDIconButton(icon="reload")

        self.play_btn.bind(on_release=self.play)
        self.pause_btn.bind(on_release=self.pause)
        self.stop_btn.bind(on_release=self.stop)
        self.reload_btn.bind(on_release=self.reload)

        self.slider.bind(value=self.seek)

        self.controls.add_widget(self.play_btn)
        self.controls.add_widget(self.pause_btn)
        self.controls.add_widget(self.stop_btn)
        self.controls.add_widget(self.reload_btn)

        self.add_widget(self.info)
        self.add_widget(self.video)
        self.add_widget(self.slider)
        self.add_widget(self.controls)

        Clock.schedule_interval(
            self.update_progress,
            0.5
        )

    # --------------------------------------------------

    def load(self, path):

        self.video.source = path
        self.info.text = path.split("/")[-1]
        self.slider.value = 0

    # --------------------------------------------------

    def play(self, *args):
        self.video.state = "play"

    # --------------------------------------------------

    def pause(self, *args):
        self.video.state = "pause"

    # --------------------------------------------------

    def stop(self, *args):
        self.video.state = "stop"
        self.video.position = 0
        self.slider.value = 0

    # --------------------------------------------------

    def reload(self, *args):

        source = self.video.source

        self.video.source = ""
        self.video.source = source

    # --------------------------------------------------

    def seek(self, instance, value):

        try:
            self.video.seek(value / 100.0)
        except Exception:
            pass

    # --------------------------------------------------

    def update_progress(self, dt):

        try:

            if self.video.duration > 0:

                self.slider.value = (
                    self.video.position /
                    self.video.duration
                ) * 100

        except Exception:
            pass

    # --------------------------------------------------

    def current_video(self):

        return self.video.source

    # --------------------------------------------------

    def is_playing(self):

        return self.video.state == "play"

    # --------------------------------------------------

    def unload(self):

        self.stop()

        self.video.source = ""
        self.info.text = "No video loaded"

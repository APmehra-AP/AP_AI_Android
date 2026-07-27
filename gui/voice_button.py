# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Reusable Voice Button
"""

from kivymd.uix.button import MDFloatingActionButton
from kivy.animation import Animation


class VoiceButton(MDFloatingActionButton):
    """
    Reusable Voice Input Button
    """

    def __init__(self, callback=None, **kwargs):
        super().__init__(**kwargs)

        self.icon = "microphone"
        self.recording = False
        self.callback = callback

        self.bind(on_release=self.toggle_recording)

    # --------------------------------------------------

    def toggle_recording(self, *args):

        if self.recording:
            self.stop_recording()
        else:
            self.start_recording()

        if callable(self.callback):
            self.callback(self.recording)

    # --------------------------------------------------

    def start_recording(self):

        self.recording = True
        self.icon = "microphone"

        self._animate()

    # --------------------------------------------------

    def stop_recording(self):

        self.recording = False
        self.icon = "microphone"

        Animation.cancel_all(self)

        self.scale_value_x = 1
        self.scale_value_y = 1

    # --------------------------------------------------

    def _animate(self):

        if not self.recording:
            return

        anim = (
            Animation(
                scale_value_x=1.15,
                scale_value_y=1.15,
                duration=0.4
            ) +
            Animation(
                scale_value_x=1.0,
                scale_value_y=1.0,
                duration=0.4
            )
        )

        anim.bind(on_complete=lambda *_: self._animate())
        anim.start(self)

    # --------------------------------------------------

    def is_recording(self):

        return self.recording

    # --------------------------------------------------

    def set_callback(self, callback):

        self.callback = callback

    # --------------------------------------------------

    def reset(self):

        self.stop_recording()

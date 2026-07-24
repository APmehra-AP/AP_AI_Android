# Created by : Amarchand Meghwal

from kivymd.uix.screen import MDScreen


class SplashScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "splash"

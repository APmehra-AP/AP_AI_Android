# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

from kivy.uix.screenmanager import FadeTransition
from kivymd.uix.screenmanager import MDScreenManager

from screens.splash import SplashScreen
from screens.home import HomeScreen


class NavigationManager(MDScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.transition = FadeTransition(duration=0.25)

        self.add_widget(SplashScreen())
        self.add_widget(HomeScreen())

        self.current = "splash"

    def open_home(self):
        self.current = "home"

    def go(self, screen_name):
        if screen_name in self.screen_names:
            self.current = screen_name
            return True
        return False

    def back_to_home(self):
        self.current = "home"

    def has_screen(self, screen_name):
        return screen_name in self.screen_names

# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Navigation Manager
"""

from kivy.uix.screenmanager import FadeTransition
from kivymd.uix.screenmanager import MDScreenManager

from screens.splash import SplashScreen
from screens.home import HomeScreen
from screens.chat import ChatScreen
from screens.settings import SettingsScreen
from screens.profile import ProfileScreen
from screens.about import AboutScreen


class NavigationManager(MDScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.transition = FadeTransition(duration=0.25)

        self.add_widget(SplashScreen())
        #self.add_widget(HomeScreen())
        #self.add_widget(ChatScreen())
        #self.add_widget(SettingsScreen())
        #self.add_widget(ProfileScreen())
        #self.add_widget(AboutScreen())

        self.current = "splash"

    # --------------------------------------------------

    def open_home(self):
        self.current = "home"

    def open_chat(self):
        self.current = "chat"

    def open_settings(self):
        self.current = "settings"

    def open_profile(self):
        self.current = "profile"

    def open_about(self):
        self.current = "about"

    # --------------------------------------------------

    def go(self, screen_name):
        """
        Open any registered screen.
        """

        if screen_name in self.screen_names:
            self.current = screen_name
            return True

        return False

    # --------------------------------------------------

    def back_to_home(self):
        self.current = "home"

    # --------------------------------------------------

    def has_screen(self, screen_name):
        return screen_name in self.screen_names

# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Main Entry Point
"""

from kivymd.app import MDApp

from screens.navigation import NavigationManager

from engine.initializer import Initializer
from engine.theme import ThemeManager


class APAI(MDApp):
    """
    AP AI Application
    """

    def build(self):

        self.title = "AP AI"

        # -------------------------------
        # Theme
        # -------------------------------

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        try:
            ThemeManager(self).apply()
        except Exception:
            pass

        # -------------------------------
        # Initialize Engine
        # -------------------------------

        try:
            Initializer().initialize()
        except Exception as e:
            print("Initialization Error:", e)

        # -------------------------------
        # Navigation
        # -------------------------------

        self.navigation = NavigationManager()

        return self.navigation

    # -----------------------------------

    def goto(self, screen):

        if self.navigation:
            self.navigation.go(screen)

    # -----------------------------------

    def home(self):
        self.goto("home")

    def chat(self):
        self.goto("chat")

    def profile(self):
        self.goto("profile")

    def settings(self):
        self.goto("settings")

    def about(self):
        self.goto("about")

    # -----------------------------------

    def on_start(self):
        print("AP AI Started")

    def on_stop(self):
        print("AP AI Closed")

    def on_pause(self):
        return True

    def on_resume(self):
        pass


if __name__ == "__main__":
    APAI().run()

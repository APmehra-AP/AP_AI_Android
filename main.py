# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

import traceback

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

from screens.navigation import NavigationManager
from engine.initializer import Initializer
from engine.theme import ThemeManager


class APAI(MDApp):

    def build(self):
        self.title = "AP AI"

        try:
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Blue"

            try:
                ThemeManager(self).apply()
            except Exception:
                pass

            try:
                Initializer().initialize()
            except Exception as e:
                print("Initialization Error:", e)

            self.navigation = NavigationManager()
            return self.navigation

        except Exception:
            error = traceback.format_exc()
            print(error)

            return MDLabel(
                text=error,
                halign="left",
                valign="top",
            )


if __name__ == "__main__":
    APAI().run()

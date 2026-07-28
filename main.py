# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

import traceback

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class APAI(MDApp):

    def build(self):
        try:
            self.title = "AP AI"

            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Blue"

            # Import only after app starts
            from screens.navigation import NavigationManager

            # ThemeManager DISABLED
            # Initializer DISABLED

            return NavigationManager()

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

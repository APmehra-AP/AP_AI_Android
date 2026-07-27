# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Reusable Bottom Navigation
"""

from kivymd.uix.navigationbar import (
    MDNavigationBar,
    MDNavigationItem,
)


class APBottomNavigation(MDNavigationBar):
    """
    Reusable Bottom Navigation Bar
    """

    def __init__(self, navigation=None, **kwargs):
        super().__init__(**kwargs)

        self.navigation = navigation

        self._add_item("Home", "home", "home")
        self._add_item("Chat", "chat", "chat")
        self._add_item("Profile", "account", "profile")
        self._add_item("Settings", "cog", "settings")

    # -------------------------------------------------

    def _add_item(self, label, icon, screen):

        item = MDNavigationItem(
            icon=icon,
            text=label
        )

        item.bind(
            on_release=lambda *_: self.open_screen(screen)
        )

        self.add_widget(item)

    # -------------------------------------------------

    def open_screen(self, screen):

        if (
            self.navigation
            and self.navigation.has_screen(screen)
        ):
            self.navigation.go(screen)

    # -------------------------------------------------

    def set_navigation(self, navigation):
        self.navigation = navigation

    # -------------------------------------------------

    def go_home(self):
        self.open_screen("home")

    def go_chat(self):
        self.open_screen("chat")

    def go_profile(self):
        self.open_screen("profile")

    def go_settings(self):
        self.open_screen("settings")

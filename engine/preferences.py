# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
User Preferences Manager
"""

from engine.settings import settings


class Preferences:

    def language(self):
        """
        Return selected language.
        """
        return settings.get("language", "hi")

    def set_language(self, language):
        """
        Set application language.
        """
        settings.set("language", language)

    def theme(self):
        """
        Return selected theme.
        """
        return settings.get("theme", "blue")

    def set_theme(self, theme):
        """
        Set application theme.
        """
        settings.set("theme", theme)

    def dark_mode(self):
        """
        Return dark mode status.
        """
        return settings.get("dark_mode", True)

    def set_dark_mode(self, enabled):
        """
        Enable or disable dark mode.
        """
        settings.set("dark_mode", bool(enabled))

    def voice_enabled(self):
        """
        Return voice status.
        """
        return settings.get("voice_enabled", True)

    def set_voice_enabled(self, enabled):
        """
        Enable or disable voice.
        """
        settings.set("voice_enabled", bool(enabled))

    def font_size(self):
        """
        Return current font size.
        """
        return settings.get("font_size", 16)

    def set_font_size(self, size):
        """
        Update font size.
        """
        settings.set("font_size", int(size))

    def animations(self):
        """
        Return animation status.
        """
        return settings.get("animations", True)

    def set_animations(self, enabled):
        """
        Enable or disable animations.
        """
        settings.set("animations", bool(enabled))

    def startup_page(self):
        """
        Return startup page.
        """
        return settings.get("startup_page", "home")

    def set_startup_page(self, page):
        """
        Set startup page.
        """
        settings.set("startup_page", page)

    def reset(self):
        """
        Restore default settings.
        """
        settings.reset()


preferences = Preferences()

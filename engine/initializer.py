# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Application Initializer
Initializes all core engine services.
"""

from engine.logger import logger
from engine.settings import settings
from engine.memory import memory
from engine.history import history
from engine.session import session
from engine.app_state import app_state
from engine.events import events
from engine.cache import cache
from engine.notifications import notifications
from engine.plugin_manager import plugins
from engine.task_manager import tasks


class AppInitializer:

    def __init__(self):
        self.initialized = False

    def initialize(self):
        """
        Initialize all core services.
        """

        if self.initialized:
            return True

        try:

            # Load managers
            settings.load()
            memory.load()

            # Reset runtime managers
            history.clear()
            session.reset()
            app_state.reset()
            cache.clear()

            # Clear temporary notifications
            notifications.clear()

            # Remove old plugins/tasks
            plugins.clear()
            tasks.cleanup()

            # Notify startup
            events.emit("app_start")

            logger.info("AP AI initialized successfully.")

            self.initialized = True

            return True

        except Exception as error:

            logger.error(
                f"Initialization failed: {error}"
            )

            return False

    def shutdown(self):
        """
        Shutdown application.
        """

        try:

            settings.save()
            memory.save()

            events.emit("app_close")

            logger.info("AP AI closed.")

            self.initialized = False

            return True

        except Exception as error:

            logger.error(
                f"Shutdown failed: {error}"
            )

            return False

    def is_initialized(self):
        """
        Return initialization status.
        """

        return self.initialized


Initializer = AppInitializer
initializer = AppInitializer()

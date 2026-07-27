# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Plugin Manager
"""

from collections import OrderedDict


class PluginManager:

    def __init__(self):
        self.plugins = OrderedDict()

    def register(self, name, plugin):
        """
        Register a plugin.
        """

        name = str(name).strip()

        self.plugins[name] = plugin

    def unregister(self, name):
        """
        Remove a plugin.
        """

        return self.plugins.pop(str(name), None)

    def exists(self, name):
        """
        Check if a plugin exists.
        """

        return str(name) in self.plugins

    def get(self, name):
        """
        Return plugin instance.
        """

        return self.plugins.get(str(name))

    def execute(self, name, *args, **kwargs):
        """
        Execute a plugin.
        """

        plugin = self.get(name)

        if plugin is None:
            return {
                "success": False,
                "message": f"Plugin '{name}' not found."
            }

        if not hasattr(plugin, "execute"):
            return {
                "success": False,
                "message": f"Plugin '{name}' has no execute() method."
            }

        try:
            result = plugin.execute(*args, **kwargs)

            return {
                "success": True,
                "result": result
            }

        except Exception as error:
            return {
                "success": False,
                "message": str(error)
            }

    def names(self):
        """
        Return plugin names.
        """

        return list(self.plugins.keys())

    def count(self):
        """
        Number of registered plugins.
        """

        return len(self.plugins)

    def clear(self):
        """
        Remove all plugins.
        """

        self.plugins.clear()


plugins = PluginManager()

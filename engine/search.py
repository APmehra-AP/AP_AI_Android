# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Search Manager
"""

import requests

from engine.network import Network


class SearchManager:

    def __init__(self):
        self.session = requests.Session()

    def web(self, query):
        """
        Basic web search placeholder.
        """

        query = str(query).strip()

        if not query:
            return {
                "success": False,
                "message": "Search query is empty."
            }

        if not Network.is_connected():
            return {
                "success": False,
                "message": "No internet connection."
            }

        return {
            "success": True,
            "query": query,
            "message": (
                "Search provider is not configured yet."
            )
        }

    def local(self, items, keyword):
        """
        Search inside a list of items.
        """

        keyword = str(keyword).lower().strip()

        results = []

        for item in items:

            text = str(item).lower()

            if keyword in text:
                results.append(item)

        return {
            "success": True,
            "count": len(results),
            "results": results
        }

    def history(self, history_items, keyword):
        """
        Search conversation history.
        """

        return self.local(
            history_items,
            keyword
        )


search = SearchManager()

# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Cache Manager
Stores temporary data in memory.
"""

import time


class CacheManager:
    def __init__(self):
        self._cache = {}

    def set(self, key, value, expire=None):
        """
        Store a value.

        expire = seconds (None means never expire)
        """

        if expire is None:
            expires_at = None
        else:
            expires_at = time.time() + expire

        self._cache[str(key)] = {
            "value": value,
            "expires": expires_at
        }

    def get(self, key, default=None):
        """
        Get cached value.
        """

        key = str(key)

        if key not in self._cache:
            return default

        item = self._cache[key]

        expires = item["expires"]

        if expires is not None and time.time() > expires:
            del self._cache[key]
            return default

        return item["value"]

    def exists(self, key):
        """
        Check if cache key exists.
        """

        return self.get(key, None) is not None

    def delete(self, key):
        """
        Remove one cache item.
        """

        self._cache.pop(str(key), None)

    def clear(self):
        """
        Clear all cache.
        """

        self._cache.clear()

    def cleanup(self):
        """
        Remove expired cache entries.
        """

        now = time.time()

        expired = [
            key
            for key, item in self._cache.items()
            if item["expires"] is not None
            and now > item["expires"]
        ]

        for key in expired:
            del self._cache[key]

    def count(self):
        """
        Number of cached items.
        """

        self.cleanup()
        return len(self._cache)

    def keys(self):
        """
        Return all valid cache keys.
        """

        self.cleanup()
        return list(self._cache.keys())


cache = CacheManager()

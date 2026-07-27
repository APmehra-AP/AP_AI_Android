# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Simple Event Manager
"""

from collections import defaultdict


class EventManager:
    def __init__(self):
        self._events = defaultdict(list)

    def on(self, event_name, callback):
        """
        Register an event listener.
        """

        if callback not in self._events[event_name]:
            self._events[event_name].append(callback)

    def off(self, event_name, callback):
        """
        Remove an event listener.
        """

        if (
            event_name in self._events
            and callback in self._events[event_name]
        ):
            self._events[event_name].remove(callback)

    def emit(self, event_name, *args, **kwargs):
        """
        Trigger an event.
        """

        if event_name not in self._events:
            return

        for callback in list(self._events[event_name]):
            try:
                callback(*args, **kwargs)
            except Exception:
                pass

    def clear(self, event_name=None):
        """
        Clear one event or all events.
        """

        if event_name is None:
            self._events.clear()
        else:
            self._events.pop(event_name, None)

    def listeners(self, event_name):
        """
        Return listeners for an event.
        """

        return list(self._events.get(event_name, []))


events = EventManager()

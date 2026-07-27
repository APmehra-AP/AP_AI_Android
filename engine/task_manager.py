# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Background Task Manager
"""

import threading


class TaskManager:
    def __init__(self):
        self.tasks = {}

    def start(self, name, target, *args, daemon=True, **kwargs):
        """
        Start a background task.
        """

        if name in self.tasks:
            task = self.tasks[name]

            if task.is_alive():
                return task

        thread = threading.Thread(
            target=target,
            args=args,
            kwargs=kwargs,
            daemon=daemon
        )

        thread.start()

        self.tasks[name] = thread

        return thread

    def running(self, name):
        """
        Check whether a task is running.
        """

        task = self.tasks.get(name)

        if task is None:
            return False

        return task.is_alive()

    def stop(self, name):
        """
        Remove finished task.

        Python threads cannot be forcefully stopped.
        """

        task = self.tasks.get(name)

        if task and not task.is_alive():
            del self.tasks[name]

    def cleanup(self):
        """
        Remove completed tasks.
        """

        finished = []

        for name, task in self.tasks.items():
            if not task.is_alive():
                finished.append(name)

        for name in finished:
            del self.tasks[name]

    def list(self):
        """
        Return running task names.
        """

        self.cleanup()

        return list(self.tasks.keys())

    def count(self):
        """
        Number of active tasks.
        """

        self.cleanup()

        return len(self.tasks)


tasks = TaskManager()

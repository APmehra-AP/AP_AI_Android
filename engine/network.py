# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Network Helper
"""

import requests

from engine.config import REQUEST_TIMEOUT


class Network:

    @staticmethod
    def is_connected():
        """
        Check internet connection.
        """

        try:
            requests.get(
                "https://www.google.com",
                timeout=5
            )
            return True

        except Exception:
            return False

    @staticmethod
    def get(url, headers=None, params=None, timeout=None):
        """
        HTTP GET
        """

        if timeout is None:
            timeout = REQUEST_TIMEOUT

        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=timeout
        )

        response.raise_for_status()

        return response

    @staticmethod
    def post(url, headers=None, json=None, data=None, timeout=None):
        """
        HTTP POST
        """

        if timeout is None:
            timeout = REQUEST_TIMEOUT

        response = requests.post(
            url,
            headers=headers,
            json=json,
            data=data,
            timeout=timeout
        )

        response.raise_for_status()

        return response

    @staticmethod
    def download(url, filename):
        """
        Download a file.
        """

        response = Network.get(url)

        with open(filename, "wb") as file:
            file.write(response.content)

        return filename

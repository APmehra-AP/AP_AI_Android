# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Security Utilities
"""

import hashlib
import secrets


class Security:
    @staticmethod
    def sha256(text):
        """
        Return SHA-256 hash.
        """

        return hashlib.sha256(
            str(text).encode("utf-8")
        ).hexdigest()

    @staticmethod
    def md5(text):
        """
        Return MD5 hash.
        """

        return hashlib.md5(
            str(text).encode("utf-8")
        ).hexdigest()

    @staticmethod
    def random_token(length=32):
        """
        Generate a secure random token.
        """

        return secrets.token_hex(length // 2)

    @staticmethod
    def mask(text, visible=4):
        """
        Hide sensitive text.

        Example:
        sk-1234567890abcdef
        ->
        **************cdef
        """

        text = str(text)

        if len(text) <= visible:
            return "*" * len(text)

        return "*" * (len(text) - visible) + text[-visible:]

    @staticmethod
    def verify_hash(text, hash_value):
        """
        Compare SHA-256 hash.
        """

        return Security.sha256(text) == hash_value

    @staticmethod
    def is_api_key(text):
        """
        Basic API key validation.
        """

        text = str(text).strip()

        return len(text) >= 20

    @staticmethod
    def safe_compare(a, b):
        """
        Constant-time comparison.
        """

        return secrets.compare_digest(
            str(a),
            str(b)
        )


security = Security()

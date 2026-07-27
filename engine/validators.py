# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Validation Utilities
"""

import re


class Validator:

    EMAIL_PATTERN = re.compile(
        r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    )

    URL_PATTERN = re.compile(
        r"^https?://.+"
    )

    @staticmethod
    def is_empty(value):
        """
        Check whether value is empty.
        """

        if value is None:
            return True

        return str(value).strip() == ""

    @staticmethod
    def is_email(email):
        """
        Validate email address.
        """

        if Validator.is_empty(email):
            return False

        return bool(
            Validator.EMAIL_PATTERN.fullmatch(
                str(email).strip()
            )
        )

    @staticmethod
    def is_url(url):
        """
        Validate URL.
        """

        if Validator.is_empty(url):
            return False

        return bool(
            Validator.URL_PATTERN.fullmatch(
                str(url).strip()
            )
        )

    @staticmethod
    def is_number(value):
        """
        Check numeric value.
        """

        try:
            float(value)
            return True
        except (TypeError, ValueError):
            return False

    @staticmethod
    def is_integer(value):
        """
        Check integer value.
        """

        try:
            int(value)
            return True
        except (TypeError, ValueError):
            return False

    @staticmethod
    def is_phone(phone):
        """
        Validate phone number.
        Accepts 10–15 digits.
        """

        phone = str(phone).replace(" ", "")

        return phone.isdigit() and 10 <= len(phone) <= 15

    @staticmethod
    def min_length(text, length):
        """
        Minimum length check.
        """

        return len(str(text)) >= length

    @staticmethod
    def max_length(text, length):
        """
        Maximum length check.
        """

        return len(str(text)) <= length

    @staticmethod
    def in_range(value, minimum, maximum):
        """
        Numeric range validation.
        """

        try:
            value = float(value)
        except (TypeError, ValueError):
            return False

        return minimum <= value <= maximum


validator = Validator()

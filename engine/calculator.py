# Created by : Amarchand Meghwal

import math


def calculate(text):

    text = text.strip()

    try:
        allowed = "0123456789+-*/().% "

        for ch in text:
            if ch not in allowed:
                return None

        return str(eval(text))

    except:
        return "❌ Invalid Calculation"


def square(value):

    try:
        num = float(value)
        return str(num * num)
    except:
        return "❌ Invalid Number"


def cube(value):

    try:
        num = float(value)
        return str(num * num * num)
    except:
        return "❌ Invalid Number"


def sqrt(value):

    try:
        num = float(value)

        if num < 0:
            return "❌ Negative Number"

        return str(math.sqrt(num))

    except:
        return "❌ Invalid Number"

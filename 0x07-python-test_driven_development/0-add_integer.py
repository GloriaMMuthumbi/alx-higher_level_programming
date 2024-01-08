#!/usr/bin/python3
"""
Module that contains a function to add two integers
"""


def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a (int or float): Operand 1
        b (int or float): Operand 2, default value is 98

    Returns:
        int: sum of a and b

    Raises:
        TypeError: If a or b is not a float or integer
        ValueError: if a or b is a NaN
        OverflowError: if a or b is an infinity
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float) and a != a:
        raise ValueError("cannot convert float Nan to integer")

    if isinstance(b, float) and b != b:
        raise ValueError("cannot convert float Nan to integer")

    if isinstance(a, float) and a == float('inf'):
        raise OverflowError("cannot convert float infinity to integer")

    if isinstance(b, float) and b == float('inf'):
        raise OverflowError("cannot convert float infinity to integer")

    a = int(a)
    b = int(b)

    return a + b

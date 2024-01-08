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
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b

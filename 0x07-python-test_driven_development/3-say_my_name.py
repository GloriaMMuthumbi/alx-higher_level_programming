#!/usr/bin/python3
"""a module that prints a string using arguments"""


def say_my_name(first_name, last_name=""):
    """
    prints "My name is <first name> <last name>"

    Args:
        first_name (str): first name
        last_name (str): last name (default to empty string)

    Raises:
        TypeError: if first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

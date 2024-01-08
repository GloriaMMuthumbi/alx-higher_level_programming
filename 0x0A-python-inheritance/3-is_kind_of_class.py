#!/usr/bin/python3
"""
checks if object is instance of specified class
or a class that has inherited
"""


def is_kind_of_class(obj, a_class):
    """
    checks if obj is an instance of a_class or a class that inherits from
    a_class

    Args:
    obj (any): the object to check
        a_class (type): class to which to match the obj with

    Returns:
        boolean: returns True is obj is an exact instance of a_class
        or a class that inherits from a_class
        otherwise - false
    """
    if isinstance(obj, a_class):
        return True
    return False

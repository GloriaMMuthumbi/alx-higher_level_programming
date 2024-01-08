#!/usr/bin/python3
"""
checks if object is an instance of a class
that inherited (directly or indirectly) from specified class
"""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of class inherited from a_class

    Args:
        obj (any): the object to check
        a_class (type): class to which to match the obj with

    Returns:
        boolean: returns True is obj is and exact instance
        otherwise - false
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

#!/usr/bin/python3
"""defines a function that checks if object is an exact instance of class"""


def is_same_class(obj, a_class):
    """
    Check if obj is an exact class of a_class

    Args:
        obj (any): the object to check
        a_class (type): class to which to match the obj with

    Returns:
        boolean: returns True is obj is and exact instance
        otherwise - false
    """
    if type(obj) == a_class:
        return True
    return False

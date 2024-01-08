#!/usr/bin/python3


def lookup(obj):
    """
    Returns a list of available attrubutes and methods of obj

    Args:
        obj: a python object

    Returns:
        list: List of available attributes and methods of obj

    """
    return [attribute for attribute in dir(obj) if not
            callable(getattr(obj, attribute))]

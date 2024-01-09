#!/usr/bin/python3

"""Defines a function to add attribute to an object"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to object if possible

    Args:
        obj: the object to which the attribute is added
        attr_name (str): the name of the attribute to be added
        attr_value: the value of the attribute to be added

    Raises:
        TypeError: if object can't have the attribute added
    """
    if not hasattr(obj, "__dict__") and not hasattr(type(obj), "__slots__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)

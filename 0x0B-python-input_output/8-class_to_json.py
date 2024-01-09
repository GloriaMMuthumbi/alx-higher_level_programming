#!/usr/bin/python3
"""defines function to convert python class to json"""


def class_to_json(obj):
    """
    returns json representation of python object
    """
    return obj.__dict__

#!/usr/bin/python3
"""defines a function that returns a JSON representation of a string object"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of string object"""
    return json.dumps(my_obj)

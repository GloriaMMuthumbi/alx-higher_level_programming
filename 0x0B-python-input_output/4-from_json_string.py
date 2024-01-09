#!/usr/bin/python3
"""defines a function to return JSON string representation"""
import json


def from_json_string(my_str):
    """returns a JSON representation of an object"""
    return json.loads(my_str)

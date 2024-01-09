#!/usr/bin/python3
"""defines a function creating an object from a json file"""
import json


def load_from_json_file(filename):
    """
    creates python object from json file
    """
    with open(filename) as file:
        return json.load(file)

#!/usr/bin/python3
"""defines a function that writes json representation to text file"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes json representation of an object to a text file
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)

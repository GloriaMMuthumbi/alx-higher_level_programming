#!/usr/bin/python3
"""
module that defines the base class
"""

import json


class Base:
    """
    manages id attribute for other classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructor for class Base

        Args:
            id (int, optional): id of instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns json string representation of list of dictionaries

        Args:
            list_dictionaries (list): List of dictionaries to convert to JSON

        Returns:
            str: JSON string representation of list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes json representation of list_objs to a file

        Args:
            list_objs (list): kist of instances to convert to JSON
            and save to file
        """
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]
        )
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        returns list of dictionatries represented by json string

        Args:
            json_string (str): JSON string representing a list of dictionaries

        Returns:
            list: List of dictionaries represented by json string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        creates and returns instance with all attributes set

        Args:
            **dictionary: dictionary containing attribute values

        Return:
            Base: instance of Base class with attributes set
        """
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)
        else:
            dummy_instance = cls()

        dummy_instance.update(**dictionary)
        return dummy_instance

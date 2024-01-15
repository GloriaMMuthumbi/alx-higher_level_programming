#!/usr/bin/python3
"""
module that defines the base class
"""

import json
import csv


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

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances based on the content of the json file

        Returns:
            list: list of instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                content = file.read()
                dictionaries = cls.from_json_string(content)
                instances = [cls.create(**d) for d in dictionaries]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        serializes list of objects to csv file

        Args:
            list_objs (list): list of instances to be serialized
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    csv_writer.writerow

    @classmethod
    def load_from_file_csv(cls):
        """
        loads instances from csv file

        Returns:
            list: list of instances loaded from file
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as file:
                csv_reader = csv.reader(file)
                instances = []
                for row in csv_reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls(
                                int(row[0]), int(row[1]),
                                int(row[2]), int(row[3]), int(row[4])
                                )
                    elif cls.__name__ == "Square":
                        instance = cls(
                                int(row[0]), int(row[1]),
                                int(row[2]), int(row[3])
                                )
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

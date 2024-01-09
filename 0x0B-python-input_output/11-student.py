#!/usr/bin/python3
"""defines a class student"""


class Student:
    """represents a student"""

    def __init__(self, first_name, last_name, age):
        """
        initializa a new student

        Args:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of student instance

        Args:
            attrs (list): list of attributes (optional)
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        replaces attributes of student

        Args:
            json (dict): the key/value pairs replacing the attributes
        """
        for key, value in json.items():
            setattr(self, key, value)

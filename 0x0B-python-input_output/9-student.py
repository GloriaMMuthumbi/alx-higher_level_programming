#!/usr/bin/python3
"""defines a class student"""


class Student:
    """represents a student"""

    def _init__(self, first_name, last_name, age):
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

    def to_json(self):
        """retrieves a dictionary representation of student instance"""
        return self.__dict__

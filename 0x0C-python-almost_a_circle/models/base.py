#!/usr/bin/python3
"""
module that defines the base class
"""


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

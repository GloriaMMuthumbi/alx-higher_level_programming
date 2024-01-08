#!/usr/bin/python3

"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class representing a square"""

    def __init__(self, size):
        """initializes class instance square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        returns a string representation of the square

        Returns:
            str: string representation of the square
        """
        return "[Square] {}.{}".format(self.width, self.height)

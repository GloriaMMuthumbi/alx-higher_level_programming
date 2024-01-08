#!/usr/bin/python3
"""defines class rectangle that inherits from BaseGeometry class"""


BaseGeometry = __import__('7-base_geomery').BaseGeometry


class Rectangle(BaseGeometry):
    """
    defines a rectangle class from the BaseGeometry class
    """

    def __init__(self, width, height):
        """
        initializes a rectangle instance

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

#!/usr/bin/python3
"""defines class rectangle that inherits from BaseGeometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns print() and str() represnetation of rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__Width) + "/" + str(self.__height)
        return string

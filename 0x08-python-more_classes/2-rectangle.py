#!/usr/bin/python3

"""Represents a rectangle class"""


class Rectangle:
    """
    Class representing a rectangle

    Attributes:
        width (int): Width of rectangle
        height (int): Height of rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializes an instance of a new Rectangle

        Args:
            width (int, optional): Width of the rectangle. Default value of 0
            height (int, optional): Height of the rectangle. Default value of 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle

        Returns:
            int: Width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle

        Args:
            value (int): Value to set the width as

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle

        Returns:
            int: Height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle

        Args:
            value (int):Value to set the height as

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Computes and returns area of the rectangle

        Returns:
            int: area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Computes and returns perimeter of the rectangel

        Returns:
            int: pertimeter of the rectangle
        """
        return (2 * (self.__width + self.__height)
                if self.__width and self.__height else 0)

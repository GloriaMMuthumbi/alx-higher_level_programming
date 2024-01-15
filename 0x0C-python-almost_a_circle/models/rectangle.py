#!/usr/bin/python3
"""
module that defines a class rectangle
"""

from models.base import Base


class Rectangle(Base):
    """
    defines rectangle class that inherits from Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        defines a constructor for the class Rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int, optional): x-coordinate of rectangle. default value of 0
            y (int, optional): y-coordinate of rectangle. default value of 0
            id (int, optional): id of rectangle. default value of None
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """getter method for width"""
            return self.__width

        @width.setter
        def width(self, value):
            """setter method for width"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be a positive integer")
            self.__width = value

        @property
        def height(self):
            """getter method for height"""
            return self.__height

        @height.setter
        def height(self, value):
            """setter method for height"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be a positive integer")
            self.__height = value

        @property
        def x(self):
            """getter method for x-coordinate"""
            return self.__x

        @x.setter
        def x(self, value):
            """setter method for x-coordinate"""
            if not isinstance(value, int):
                raise TypeError("x must be an integer")
            if value <= 0:
                raise ValueError("x must be a none-negative integer")
            self.__x = value

        @property
        def y(self):
            """getter method for y-coordinate"""
            return self.__y

        @y.setter
        def y(self, value):
            """setter method for y-coordinate"""
            if not isinstance(value, int):
                raise TypeError("y must be an integer")
            if value <= 0:
                raise ValueError("y must be a none-negative integer")
            self.__y = value

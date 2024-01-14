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
        super().__init__*(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


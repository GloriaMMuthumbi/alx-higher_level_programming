#!/usr/bin/python3
"""module defines the sqquare class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """defines class square inheriting from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        defines constructor for square class

        Args:
            size (int): size of square
            x (int, optional): x-coordinate of square. default value of 0
            y (int, optional): y-coordinate of square. default value of 0
            id (int, optional): id of square. default value of None
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter method for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter method for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """returns a string representationg of the square instance"""
        return "[Square] ({}) {}/{} - {}". format(
                self.id, self.x, self.y, self.width
                )

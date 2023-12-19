#!/usr/bin/python3
"""Module documentation for Square class."""


class Square:
    """Square class definition"""

    def __init__(self, size=0):
        """Initialise instance of square

        Args:
            size (int): size of square.

        Raises:
            TypeError: if size is not an int
            ValueError: if size is less than 0
        """
        self.size = size

    @property
    def size(self):
        """Getter function for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter function for size

        Args:
            value (int): value to be set as size

        Raises:
            TypeError: If value is not an int
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calulates the are of square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

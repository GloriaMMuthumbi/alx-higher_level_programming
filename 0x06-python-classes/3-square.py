#!/usr/bin/python3
"""Documentation for Square class."""


class Square:
    """Defines the square."""

    def __init__(self, size=0):
        """Initialize instance of square.

        Args:
            size (int): The size of the quare

        Raises:
            TypeError: If size is not int
            ValueError: If sie is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of square.

        Returns:
            int: The are of the square.
        """
        return self.__size ** 2

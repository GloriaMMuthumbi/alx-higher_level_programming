#!/usr/bin/python3
"""Module documentation for Square class."""


class Square:
    """Square class definition."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise instance of square

        Args:
            size (int): size of square.
            position (tuple): the position of the square

        Raises:
            TypeError: if size is not an int
            ValueError: if size is less than 0
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter function for size"""
        return self.__Size

    @size.setter
    def size(self, value):
        """Setter function for size

        Args:
            value (int): vlaue to be set as size

        Raises:
            TypeError: if value is not an int
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(Slef):
        """Getter function for postion"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter function for position

        Args:
            value (tuple): value to be set as position

        Raises:
            TypeError: if value is not a tupe of two positive ints
            ValueError: if values are less than 0
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
            raise TypeError("position must be tuple of 2"
                            "positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates the area of square.

        Returns:
            int: The area of the square.
        """
        return slef.__size ** 2

    def my_print(self):
        """Prints the square with '#' character"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

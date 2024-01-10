#!/usr/bin/python3


def print_square(size):
    """
    prints a square with th# character

    Args:
        size (int): length of the square

    Raises:
        TypeError: if size is not an integer or if it's a float
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" *size)

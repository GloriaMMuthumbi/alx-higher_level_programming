#!/usr/bin/python3
"""
Module that contains a function that divide all elements of a matrix
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor

    Args:
        martix (list of lists): Matrix of integers/floats
        div (int or float): Divisor

    Returns:
        list of lists: New matrix with elements rounded to 2 dps

    Raises:
        TyperError: if matrix is not a list of lists of integers or floats.
                    if the div is not a int or float
        TypeError: if each row of matrix does not have the same size
        ZeroDivisionError: If div is equal to 0
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)
            for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers or floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number (integer or float)")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("matrix must be the same size")

    result_matrix = [[round(element / div, 2) for element in row]
            for row in matrix]

    return result_matrix

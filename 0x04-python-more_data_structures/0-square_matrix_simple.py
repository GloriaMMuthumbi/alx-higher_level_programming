#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_matrix = [[0] * len(row) for row in matrix]
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            result_matrix[row][column] = matrix[row][column] ** 2
    return result_matrix

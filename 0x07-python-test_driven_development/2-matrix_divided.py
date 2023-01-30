#!/usr/bin/python3
"""Divide Matrix Module"""


def matrix_divided(matrix, div):
    """Divides matrix by number div"""

    result = []

    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len(matrix) < 1 or len(matrix[0]) < 1:
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
    for i in matrix:
        if len(i) != len(matrix[1]):
            raise TypeError("Each row of the matrix must have the same size")
    for i in range(len(matrix)):
        result.append([])
        for j in range(len(matrix[i])):
            if isinstance(matrix[i][j], (int, float)) is False:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
            else:
                result[i].append(round((matrix[i][j] / div), 2))
    return result

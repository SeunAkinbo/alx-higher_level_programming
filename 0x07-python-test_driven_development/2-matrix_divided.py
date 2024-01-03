#!/usr/bin/python3

"""
Description: The module divides all elements of a matrix
Module: 2-matrix_divided
Function: matrix_divided
"""


def matrix_divided(matrix, div):
    """
    Parameters:
    - matrix (list of integer): List of a list
    - div (integer): The divisor
    """

    """Validate matrix"""
    if not isinstance(matrix, list) or not matrix or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")

    if not all(isinstance(num, (float, int)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")

    """Validate row sizes"""
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    """Validate div"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    """Validate non-zero div"""
    if div == 0:
        raise ZeroDivisionError("division by zero")

    """Perform division and rounding"""
    result = [[round(num / div, 2) for num in row] for row in matrix]

    return result

#!/usr/bin/python3
"""Documentation for a matrix division function"""


def matrix_divided(matrix, div):
    """Function divides a matrix by an integer or float

    Args:
       matrix (list): the matrix to divide
       div (int or float): the number to divide the matrix by

    Returns:
       new matrix containing the divided numbers
    """
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/\
        floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists of integers)/\
        floats")
    if type(matrix) == tuple or type(matrix) == set:
        raise TypeError("matrix must be a matrix (list of lists of integers)/\
        floats")
    for i in matrix:
        if len(i) == 0:
            raise TypeError("matrix must be a matrix(list of lists of integers)
                            floats")
        if type(i) == tuple or type(i) == set:
            raise TypeError("matrix must be a matrix(list of lists of integers)
                            floats")
    if div == 0:
        raise ZeroDivisionError("dividion by zero")
    if isinstance(div, int) is False and isinstance(div, float) is False:
        raise TypeError("div must be a number")
    length = len(matrix[0])
    for matrices in matrix:
        if len(matrices) != length:
            raise TypeError("Each row of the matrix must have the same size")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                raise TypeError("Matrix must be a matrix (list of lists) of \
                                integers/floats")
    new_matrix = []
    for i in matrix:
        new_matrix.append(list(map(lambda x: round(x / div, 2), i)))
    return new_matrix

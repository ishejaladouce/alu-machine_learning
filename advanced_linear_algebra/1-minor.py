#!/usr/bin/env python3
"""Function that calculates the minor matrix of a matrix"""


def determinant(matrix):
    """Function that calculates the determinant of a matrix"""
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    det = 0
    for col in range(len(matrix)):
        sub = [row[:col] + row[col + 1:] for row in matrix[1:]]
        sign = 1 if col % 2 == 0 else -1
        det += sign * matrix[0][col] * determinant(sub)
    return det


def minor(matrix):
    """Function that calculates the minor matrix of a matrix"""
    if type(matrix) is not list or len(matrix) == 0 or \
            not all(type(row) is list for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if len(matrix) == 1:
        return [[1]]

    result = []
    for i in range(len(matrix)):
        result_row = []
        for j in range(len(matrix)):
            sub = [row[:j] + row[j + 1:]
                   for k, row in enumerate(matrix) if k != i]
            result_row.append(determinant(sub))
        result.append(result_row)
    return result

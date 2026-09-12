#!/usr/bin/env python3
"""Transposes a 2D matrix."""


def matrix_transpose(matrix):
    """Returns a new matrix with rows and columns swapped."""
    new_matrix = []
    for col in range(len(matrix[0])):
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][col])
        new_matrix.append(new_row)
    return new_matrix

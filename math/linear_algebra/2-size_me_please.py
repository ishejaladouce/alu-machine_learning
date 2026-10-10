#!/usr/bin/env python3
"""Finds the shape of a matrix."""


def matrix_shape(matrix):
    """Returns the shape of a matrix as a list of integers."""
    shape = []
    while type(matrix) is list:
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape

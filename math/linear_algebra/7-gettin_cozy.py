#!/usr/bin/env python3
"""Concatenates two 2D matrices along an axis."""


def cat_matrices2D(mat1, mat2, axis=0):
    """Returns a new matrix, or None if the shapes do not fit."""
    result = []
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        for row in mat1 + mat2:
            result.append(row[:])
        return result
    if len(mat1) != len(mat2):
        return None
    for i in range(len(mat1)):
        result.append(mat1[i] + mat2[i])
    return result

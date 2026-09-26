#!/usr/bin/env python3
"""Joins two numpy arrays along an axis."""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Returns a new numpy array with both joined together."""
    return np.concatenate((mat1, mat2), axis=axis)

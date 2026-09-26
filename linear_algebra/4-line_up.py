#!/usr/bin/env python3
"""Adds two arrays element-wise."""


def add_arrays(arr1, arr2):
    """Returns a new list with the sums, or None if sizes differ."""
    if len(arr1) != len(arr2):
        return None
    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[i])
    return result

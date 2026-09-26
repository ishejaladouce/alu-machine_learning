#!/usr/bin/env python3
"""Does element-wise math on two numpy arrays."""


def np_elementwise(mat1, mat2):
    """Returns the sum, difference, product and quotient as a tuple."""
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)

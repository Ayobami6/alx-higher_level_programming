#!/usr/bin/python3
""" Matix_multiply module
"""
import numpy as np


def lazy_matrix_mul(m_a: list, m_b: list) -> list:
    """ Matrix Multiply

    Args:
        m_a (list): list of list
        m_b (list): list of list

    Returns:
        list: list
    """
    result = np.matmul(m_a, m_b)
    return result

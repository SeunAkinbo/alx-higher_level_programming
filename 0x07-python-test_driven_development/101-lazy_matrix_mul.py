#!/usr/bin/python3
'''Multiplying matrices using NumPy'''
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    '''Multiplying 2 matrices using numpy
    Args:
        - m_a (list of integers or floats)
        - m_b (list of integers or floats)
    '''
    return np.dot(m_a, m_b)

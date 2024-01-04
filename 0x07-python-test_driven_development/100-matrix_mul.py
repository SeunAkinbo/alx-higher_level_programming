#!/usr/bin/python3

'''100-matrix_mul module
Function: matrix_mul
'''


def matrix_mul(m_a, m_b):
    '''Multiplies two matrices.
    Args:
        - m_a (list of integers or floats)
        - m_b (list of integers or floats)
    '''
    if not isinstance(m_a, list) or not all(
            isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not isinstance(m_b, list) or not all(
            isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a or not all(m_a):
        raise ValueError("m_a can't be empty")

    if not m_b or not all(m_b):
        raise ValueError("m_b can't be empty")

    if any(not all(isinstance(
            num, (int, float)) for num in row) for row in m_a):
        raise TypeError("m_a should contain only integers or floats")

    if any(not all(isinstance(
            num, (int, float)) for num in row) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a[1:] + m_b):
        raise TypeError("each row of m_a must be of the same size "
                        "or each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[sum(a * b for a, b in zip(row_a, col_b))
               for col_b in zip(*m_b)] for row_a in m_a]

    return result

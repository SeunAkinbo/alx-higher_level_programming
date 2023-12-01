#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Looping through the list
    for row in matrix:
        # Unpacking the list using the * anad printing to the stdout
        print(*row)

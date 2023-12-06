#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sort = sorted(a_dictionary)
    for item in sort:
        print(f"{item}: {a_dictionary[item]}")

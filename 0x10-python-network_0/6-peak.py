#!/usr/bin/python3
"""Module 6-peak"""


def find_peak(list_of_integers):
    """The function finds the peak in a list of unsorted integers"""
    if len(list_of_integers) != 0 :
        sort_list = sorted(list_of_integers)
        return sort_list[len(list_of_integers) - 1]
    else:
        return None

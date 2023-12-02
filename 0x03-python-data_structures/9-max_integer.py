#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    for num in my_list:
        max_num = -1000
        if num > max_num:
            max_num = num
    return max_num

#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list:
        numerator = [int(row[0]) * int(row[1]) for row in my_list]
        denominator = [int(row[1]) for row in my_list]
        return sum(numerator) / sum(denominator)
    else:
        return 0

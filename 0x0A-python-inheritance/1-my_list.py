#!/usr/bin/python3

'''Module: 1-my_list.py'''


class MyList(list):
    '''Class that inherits from list'''

    def print_sorted(self):
        '''class method that prints a sorted list'''
        sorted_list = sorted(self)
        print(sorted_list)

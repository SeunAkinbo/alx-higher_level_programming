#!/usr/bin/python3
'''Moduled: 100-my_int.py'''


class MyInt(int):
    '''MyInt class that inherits from int'''

    def __eq__(self, other):
        '''Inverts the == operator.
        Args:
            - other (integer): for comparison
        return: True in not equal, False if equal
        '''
        return super().__ne__(other)

    def __ne__(self, other):
        '''Inverts the != operator.
        Args:
            - other (integer): for comparison
        return: True if equal, False if not equal
        '''
        return super().__eq__(other)

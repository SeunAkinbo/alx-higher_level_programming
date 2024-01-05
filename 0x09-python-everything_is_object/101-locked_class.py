#!/usr/bin/python3
class LockedClass:
    '''Prevents dynamic attribute creation except for first_name'''
    __slots__ = ["first_name"]

    def __setattr__(self, name, value):
        '''Restricts attribute setting'''
        if name != "first_name":
            raise AttributeError(f"'LockedClass' object has no "
                                 f"attribute '{name}'")
        super().__setattr__(name, value)

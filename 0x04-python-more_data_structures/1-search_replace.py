#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # return list(map(lambda x: 89 if x == 2 else x, my_list))
    def update(item):
        return item if item != search else replace
    return list(map(update, my_list))

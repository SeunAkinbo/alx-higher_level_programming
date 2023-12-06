#!/usr/bin/python3

def search_replace(my_list, search, replace):
    def update(item):
        return item if item != search else replace
    return list(map(update, my_list))

#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    sorted_list = sorted(my_list)
    count = len(sorted_list) - 1
    return sorted_list[count]

#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set()
    for element in my_list:
        unique.add(element)
    result = sum(unique)
    return result

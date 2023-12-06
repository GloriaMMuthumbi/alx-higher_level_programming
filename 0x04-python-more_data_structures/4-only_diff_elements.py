#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    result = set()
    common_set = set_1 & set_2
    for element in set_1:
        if element not in common_set:
            result.add(element)
    for element in set_2:
        if element not in common_set:
            result.add(element)
    return result

#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    original_list = my_list.copy()
    if idx < 0 or idx > len(my_list):
        return (original_list)
    else:
        new_list = my_list.copy()
        del new_list[idx]
        return (new_list)

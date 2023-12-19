#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        value = my_list[i]
        try:
            print("{:d}".format(value), end="")
        except (TypeError, ValueError):
            pass
        else:
            count += 1
    print()
    return count

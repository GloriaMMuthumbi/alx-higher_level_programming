#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value = "{:d}".format(value)
        print(value)
        return True
    except ValueError:
        return False

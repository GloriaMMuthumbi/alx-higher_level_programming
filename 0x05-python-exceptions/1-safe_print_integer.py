#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            raise TypeError("Value is not an integer")
    except (ValueError, TypeError):
        return False

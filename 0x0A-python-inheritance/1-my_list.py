#!/usr/bin/python3
"""This module creates a class that inherits from list class"""


class MyList(list):
    """
    a class that inherits from built-in class list.
    """
    def print_sorted(self):
        """
        Prints list in ascending order

        Returns:
            None
        """
        sorted_list = sorted(self)
        print(sorted_list)

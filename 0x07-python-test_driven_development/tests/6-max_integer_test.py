#!/usr/bin/python3
"""Unitest for max_intefer([..])
"""
import unittest
max_int = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])"""

    def unordered_list_test(self):
        """tests an unordered list of integer"""
        ul = [2, 1, 4, 3]
        self.assertEqual(max_integer(ul), 4)

    def ordered_list_test(self):
        """tests an ordered list of integer"""
        ol = [1, 2, 3, 4]
        self.assertEqual(max_integer(ol), 4)

    def one_element_list_test(self):
        """tests a single element list of integer"""
        one_l = [2]
        self.assertEqual(max_integer(one_l), 4)

    def floats_list_test(self):
        """tests list of floats"""
        fl = [2.9, 1.23, 4.45, 3.88]
        self.assertEqual(max_integer(fl), 4)

    def empty_list_test(self):
        """tests an empty list"""
        empty_l = []
        self.assertEqual(max_integer(empty_l), 4)

    def unordered_list_test(self):
        """tests an unordered list of integer"""
        ul = [2, 1, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def mixed_list_test(self):
        """tests a mixed list of integer"""
        mixed_l = [2, 1.509, -4, 3.9]
        self.assertEqual(max_integer(mixed_l), 4)

    def string_list_test(self):
        """tests a string list of integer"""
        str_l = ["2", "1", "4", "3"]
        self.assertEqual(max_integer(str_l), 4)


if __name__ == '__main__':
    unittest.main()

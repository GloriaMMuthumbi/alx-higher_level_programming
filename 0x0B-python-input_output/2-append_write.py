#!/usr/bin/python3
"""defines a function that appends a sting at the end of text file"""


def append_write(filename="", text=""):
    """
    appends a string to end of a text file

    Args:
        filename (str): name of the file to append string to
        text (sts): string to be appended to file

    Return:
        number of characters appended to file
    """
    with open(filename, 'a', encoding='utf-8') as file:
        appended_chars = file.write(text)
        return appended_chars

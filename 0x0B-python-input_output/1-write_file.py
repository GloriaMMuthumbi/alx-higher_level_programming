#!/usr/bin/python3
"""defines a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """
    writes a string to a utf-8 text file

    Args:
        filename (str): the name of the file to write
        text (str): the text to write in the file

    Returns:
        number of characters written in file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_of_chars = file.write(text)
        return num_of_chars

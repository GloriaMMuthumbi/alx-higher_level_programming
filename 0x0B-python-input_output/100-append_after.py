#!/usr/bin/python3
"""defines a function that inserts a line of text into a file"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts text after each line containing a given string in file

    Args:
        filename (Str): name of the file
        search_string (str_): string to search for in file
        new_string (str): string to insert
    """
    text = ""
    with open(filename) as read_file:
        for line in read_file:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, 'w') as write_file:
        write_file.write(text)

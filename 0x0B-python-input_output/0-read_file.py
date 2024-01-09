#!/usr/bin/python3
"""defines function that reads contents from a file"""

def read_file(filename=""):
    """
    Read a text file (UTF-8) and print out it's contents to stdout
    """
    with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content, end="")

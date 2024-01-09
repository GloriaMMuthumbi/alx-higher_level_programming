#!/usr/bin/python3

def read_file(filename=""):
    """
    Read a text file (UTF-8) and print out it's contents to stdout

    Args:
        filename (str): name of the file to be read
    """
    with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content, end="")

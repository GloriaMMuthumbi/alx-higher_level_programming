#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            new_str += "{}".format(chr(ord(char) - ord('a') + ord('A')))
        else:
            new_str += "{}".format(char)
    print(new_str)

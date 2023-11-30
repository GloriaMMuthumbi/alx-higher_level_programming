#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    n = len(argv) - 1
    if n != 1:
        print("{:d} arguments".format(n), end="")
    else:
        print("{:d} argument".format(n), end="")
    args = argv[1:]
    if n == 0:
        print(".")
    else:
        print(":")

    for i in range(n):
        print("{}: {}".format(i + 1, args[i]))

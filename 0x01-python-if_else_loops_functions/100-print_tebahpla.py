#!/usr/bin/python3
for char in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(char - ord('a') + ord('A'))
          if char % 2 != 0 else chr(char)), end='')

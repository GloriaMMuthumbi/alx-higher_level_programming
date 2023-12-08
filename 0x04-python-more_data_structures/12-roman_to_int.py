#!/usr/bin/python3
def roman_to_int(roman_string):
    if (type(roman_string) is not str) or (roman_string is None):
        return 0
    roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
    length = len(roman_string)
    result = romans[roman_string[length-1]
    for c in range(length - 1, 0, -1):
        value = roman_dic[roman_string[c]]
        prev = roman_dic[roman_string[c-1]]
        if value < prev:
            result -= prev
        else:
            result += prev
    return result

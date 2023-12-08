#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)
    roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev = 0
    for c in range(len(roman_string) -1, 0, -1):
        value = roman_dic[roman_string[c]]
        if value < prev:
            result -= value
        else:
            result += value
        pre = value
    return (result)

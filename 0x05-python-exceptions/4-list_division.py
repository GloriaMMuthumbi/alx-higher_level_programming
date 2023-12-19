#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            result = num1 / num2
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by zero")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
    return new_list

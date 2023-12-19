#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except (TypeError):
            print("Error: Wrong Type")
            result = 0
        except (ZeroDivisionError):
            print("Error: Division by Zero")
            result = 0
        except (IndexError):
            print("Error: Index out of range")
            result = 0
        finally:
            new_list.append(result)
        return(new_list)

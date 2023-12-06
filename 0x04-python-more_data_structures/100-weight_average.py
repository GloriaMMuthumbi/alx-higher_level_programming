#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weight_sum = sum(score * weight for score, weight in my_list)
    weight_total = sum(weight for _, weight in my_list)
    return weight_sum / weight_total

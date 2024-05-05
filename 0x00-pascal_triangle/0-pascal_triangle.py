#!/usr/bin/python3
"""Create a function def pascal_triangle(n):
that returns a list of lists of integers representing
the Pascal’s triangle of n"""
import math


def pascal_triangle(n):
    """return list of lists of integers representing the Pascal’s triangle"""
    if (n <= 0):
        return []
    P_list = []
    for i in range(n):
        R_list = []
        for j in range(i + 1):
            element = math.factorial(i) // (math.factorial(j) * math.factorial(i - j))
            R_list.append(element)
        P_list.append(R_list)
    return P_list

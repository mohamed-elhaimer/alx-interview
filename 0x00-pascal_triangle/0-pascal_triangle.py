#!/usr/bin/python3
"""Create a function def pascal_triangle(n):
that returns a list of lists of integers representing
the Pascal’s triangle of n"""


def factoriel(n):
    if n == 0:
        return 1
    else:
        return n * factoriel(n - 1)


def pascal_triangle(n):
    """return list of lists of integers representing the Pascal’s triangle"""
    if (n <= 0):
        return []
    P_list = []
    for i in range(n):
        R_list = []
        for j in range(i + 1):
            element = factoriel(i) // (factoriel(j) * factoriel(i - j))
            R_list.append(element)
        P_list.append(R_list)
    return P_list

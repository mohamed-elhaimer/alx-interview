#!/usr/bin/python3
""" method that determines if all the boxes can be opened."""
from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """return true if all boxes opned otherwise return false"""
    n = len(boxes)
    opend = [False] * n
    opend[0] = True
    stack = [0]
    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < n and not opend[key]:
                opend[key] = True
                stack.append(key)
    return all(opend)

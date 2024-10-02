#!/usr/bin/python3
"""
function that returns a list of lists of integers
representing the pascal's triangle of n:
"""


def pascal_triangle(n):
    """ the function """
    if n <= 0:
        return []
    tri = [[1]]
    for x in range(1, n):
        row =[1]
        for y in range(1, x):
            row.append(tri[x-1][y-1] + tri[x-1][y])
        row.append(1)
        tri.append(row)
    return tri

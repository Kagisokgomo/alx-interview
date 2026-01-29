#!/usr/bin/python3
"""
0-pascal_triangle
Generates Pascal's Triangle of n rows
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        prev_row = triangle[-1]
        # Generate new row
        row = [1]  # First element
        for j in range(1, len(prev_row)):
            row.append(prev_row[j-1] + prev_row[j])
        row.append(1)  # Last element
        triangle.append(row)

    return triangle

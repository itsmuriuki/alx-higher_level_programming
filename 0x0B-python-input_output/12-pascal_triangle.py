#!/usr/bin/python3
"""Documentation for a pascal_triangle function"""


def pascal_triangle(n):
    """Prints a list of lists of a pascal triangle

    Args:
        n (int): the number of row of the Pascal Triangle

    Returns:
        The Pascal Triangle as a list of lists
    """

    triangle = []
    prev_row = [1]
    row = 0
    if n <= 0:
        return []
    triangle.append(prev_row)
    if n == 1:
        return triangle
    while row < n - 1:
        current_row = []
        current_row.append(prev_row[0])
        i = 0
        while i < row:
            current_row.append(prev_row[i] + prev_row[i + 1])
            i += 1
        current_row.append(prev_row[len(prev_row) - 1])
        triangle.append(current_row)
        prev_row = current_row
        row += 1
    return triangle
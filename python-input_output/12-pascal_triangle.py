#!/usr/bin/python3
"""Pascal's Triangle."""


def pascal_triangle(n):
    """Return Pascal's triangle of n."""
    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) < n:
        prev = triangle[-1]
        row = [1]

        for i in range(len(prev) - 1):
            row.append(prev[i] + prev[i + 1])

        row.append(1)
        triangle.append(row)

    return triangle

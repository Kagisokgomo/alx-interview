#!/usr/bin/python3
"""
0-minoperations
This module defines a function to calculate the minimum number of
Copy All and Paste operations to get exactly n H's.
"""

def minOperations(n):
    """
    Returns the minimum number of operations to get n H's
    starting from 1 H using only Copy All and Paste.

    Args:
        n (int): Target number of H's.

    Returns:
        int: Minimum number of operations, or 0 if impossible.
    """
    if n < 2:
        return 0  # Impossible or already 1 H

    operations = 0
    i = 2
    while i <= n:
        while n % i == 0:
            operations += i
            n //= i
        i += 1

    return operations

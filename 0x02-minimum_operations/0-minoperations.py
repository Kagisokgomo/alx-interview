#!/usr/bin/python3
"""
0-minoperations
Calculates the minimum number of Copy All and Paste operations
to reach exactly n H's starting from 1 H.
"""

def minOperations(n):
    """
    Return the minimum number of operations to get n H's.

    Args:
        n (int): Target number of H's.

    Returns:
        int: Minimum number of operations. Returns 0 if impossible.
    """
    if n <= 1:
        return 0  # Already 1 H or impossible

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations

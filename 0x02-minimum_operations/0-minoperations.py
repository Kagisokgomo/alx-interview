#!/usr/bin/python3
"""
0-minoperations
Calculates the fewest number of operations needed
to result in exactly n H characters in a text file.
"""

def minOperations(n):
    """
    Return the minimum number of operations to get n H's
    using only Copy All and Paste.

    Args:
        n (int): Target number of H's.

    Returns:
        int: Minimum number of operations. Returns 0 if n <= 1.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations

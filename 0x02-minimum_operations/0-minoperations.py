#!/usr/bin/python3
"""
0-minoperations
Calculate the minimum number of operations to get n H's
"""

def minoperations(n):
    """
    Returns the minimum number of operations to get n H's
    using only Copy All and Paste.

    Args:
        n (int): Target number of H's

    Returns:
        int: Minimum number of operations, or 0 if impossible
    """
    if n < 2:
        return 0  # Impossible to reach 1 H (already have 1 H)
    
    operations = 0
    i = 2
    while i <= n:
        while n % i == 0:
            operations += i
            n //= i
        i += 1
    return operations

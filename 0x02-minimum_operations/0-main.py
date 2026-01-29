#!/usr/bin/python3
"""
Main file for testing
"""

minoperations = __import__('0-minoperations').minoperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minoperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minoperations(n)))

"""Test file for 15_second_largest.py"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Test_Code._import_helper import load_module

mod = load_module("Code/15_second_largest.py")
second_largest = mod.second_largest

# Normal cases
assert second_largest([1, 2, 3]) == 2
assert second_largest([3, 1, 4, 1, 5, 9, 2, 6]) == 6
assert second_largest([10, 5, 8, 3]) == 8

# With duplicates of the largest value
assert second_largest([10, 10, 9]) == 9
assert second_largest([5, 5, 5, 4]) == 4

# Two distinct values
assert second_largest([1, 2]) == 1
assert second_largest([2, 1]) == 1

# Negative numbers
assert second_largest([-1, -2, -3]) == -2

# Mix of negative and positive
assert second_largest([-10, 0, 5, 3]) == 3

# Only one distinct value must raise ValueError
try:
    second_largest([5, 5, 5])
    raise AssertionError("Expected ValueError for all same values")
except ValueError:
    pass

# Empty list must raise ValueError (fewer than two distinct)
try:
    second_largest([])
    raise AssertionError("Expected ValueError for empty list")
except (ValueError, Exception):
    pass

# Single element must raise ValueError
try:
    second_largest([7])
    raise AssertionError("Expected ValueError for single element")
except ValueError:
    pass

print("All test cases passed.")

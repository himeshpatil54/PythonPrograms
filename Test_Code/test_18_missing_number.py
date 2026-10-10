"""Test file for 18_missing_number.py"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Test_Code._import_helper import load_module

mod = load_module("Code/18_missing_number.py")
find_missing_number = mod.find_missing_number

# Missing at the beginning (0 is missing)
assert find_missing_number([1, 2, 3, 4, 5]) == 0

# Missing in the middle
assert find_missing_number([0, 1, 3, 4, 5]) == 2
assert find_missing_number([0, 2, 3, 4, 5]) == 1
assert find_missing_number([0, 1, 2, 4, 5]) == 3

# Missing at the end
assert find_missing_number([0, 1, 2, 3, 4]) == 5

# Minimum case: one element, one missing
assert find_missing_number([1]) == 0
assert find_missing_number([0]) == 1

# Duplicate values must raise ValueError
try:
    find_missing_number([0, 1, 1, 3])
    raise AssertionError("Expected ValueError for duplicates")
except ValueError:
    pass

# Out-of-range value must raise ValueError
try:
    find_missing_number([0, 1, 10])
    raise AssertionError("Expected ValueError for out-of-range value")
except ValueError:
    pass

# Empty list must raise ValueError
try:
    find_missing_number([])
    raise AssertionError("Expected ValueError for empty list")
except ValueError:
    pass

print("All test cases passed.")

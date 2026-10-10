"""Test file for 19_find_duplicates.py"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Test_Code._import_helper import load_module

mod = load_module("Code/19_find_duplicates.py")
find_duplicates = mod.find_duplicates

# Normal case
assert find_duplicates([1, 2, 3, 2, 4, 3, 5]) == [2, 3]

# All same element — returned only once
assert find_duplicates([1, 1, 1, 1]) == [1]

# No duplicates
assert find_duplicates([1, 2, 3]) == []

# Empty list
assert find_duplicates([]) == []

# Order of first becoming duplicate preserved
assert find_duplicates([3, 1, 3, 2, 2, 4]) == [3, 2]

# Strings
assert find_duplicates(["a", "b", "a", "c", "b"]) == ["a", "b"]

# Multiple duplicates, each reported once
assert find_duplicates([5, 5, 5, 6, 6]) == [5, 6]

# Single element, no duplicate
assert find_duplicates([42]) == []

print("All test cases passed.")

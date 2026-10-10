"""Test file for 16_remove_duplicates.py"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Test_Code._import_helper import load_module

mod = load_module("Code/16_remove_duplicates.py")
remove_duplicates = mod.remove_duplicates

# Normal case: duplicates removed, order preserved
assert remove_duplicates([1, 2, 3, 2, 1, 4]) == [1, 2, 3, 4]

# Strings
assert remove_duplicates(["a", "b", "a", "c"]) == ["a", "b", "c"]

# Empty list
assert remove_duplicates([]) == []

# All duplicates
assert remove_duplicates([1, 1, 1]) == [1]

# No duplicates (unchanged)
assert remove_duplicates([1, 2, 3]) == [1, 2, 3]

# Mixed types
assert remove_duplicates([1, "a", 1, "b", "a"]) == [1, "a", "b"]

# Order of first occurrence preserved
assert remove_duplicates([3, 1, 2, 1, 3]) == [3, 1, 2]

print("All test cases passed.")

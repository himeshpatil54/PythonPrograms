"""Test file for 17_common_elements.py"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Test_Code._import_helper import load_module

mod = load_module("Code/17_common_elements.py")
common_elements = mod.common_elements

# Normal case
assert common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]

# Order follows list1's first appearance
assert common_elements([4, 3, 2, 1], [1, 2]) == [2, 1]

# Duplicates in list1: returned only once
assert common_elements([1, 2, 2, 3], [2, 3, 4]) == [2, 3]

# Empty list1
assert common_elements([], [1, 2]) == []

# Empty list2
assert common_elements([1, 2], []) == []

# Both empty
assert common_elements([], []) == []

# No common elements
assert common_elements([1, 2, 3], [4, 5, 6]) == []

# All common
assert common_elements([1, 2, 3], [1, 2, 3]) == [1, 2, 3]

# Strings
assert common_elements(["a", "b", "c"], ["b", "c", "d"]) == ["b", "c"]

print("All test cases passed.")

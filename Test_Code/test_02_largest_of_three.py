"""Test file for 02_largest_of_three.py"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Test_Code._import_helper import load_module

mod = load_module("Code/02_largest_of_three.py")
largest_of_three = mod.largest_of_three

# Normal cases
assert largest_of_three(1, 2, 3) == 3
assert largest_of_three(10, 5, 8) == 10
assert largest_of_three(3, 7, 5) == 7

# All equal (tie)
assert largest_of_three(4, 4, 4) == 4

# Two equal, one larger
assert largest_of_three(5, 5, 9) == 9
assert largest_of_three(9, 5, 5) == 9

# Negative numbers
assert largest_of_three(-1, -2, -3) == -1
assert largest_of_three(-5, 0, -3) == 0

# Mix of positive and negative
assert largest_of_three(-10, 100, 50) == 100

print("All test cases passed.")

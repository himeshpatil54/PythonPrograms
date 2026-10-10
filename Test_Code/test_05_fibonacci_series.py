"""Test file for 05_fibonacci_series.py"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Test_Code._import_helper import load_module

mod = load_module("Code/05_fibonacci_series.py")
fibonacci_series = mod.fibonacci_series

# Boundary: n=0 returns []
assert fibonacci_series(0) == []

# n=1 returns [0]
assert fibonacci_series(1) == [0]

# n=2 returns [0, 1]
assert fibonacci_series(2) == [0, 1]

# Normal cases
assert fibonacci_series(5) == [0, 1, 1, 2, 3]
assert fibonacci_series(8) == [0, 1, 1, 2, 3, 5, 8, 13]
assert fibonacci_series(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Negative input must raise ValueError
try:
    fibonacci_series(-1)
    raise AssertionError("Expected ValueError for fibonacci_series(-1)")
except ValueError:
    pass

try:
    fibonacci_series(-5)
    raise AssertionError("Expected ValueError for fibonacci_series(-5)")
except ValueError:
    pass

print("All test cases passed.")

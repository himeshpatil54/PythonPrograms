"""Test file for 04_factorial.py"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Test_Code._import_helper import load_module

mod = load_module("Code/04_factorial.py")
factorial = mod.factorial

# Base cases
assert factorial(0) == 1
assert factorial(1) == 1

# Normal cases
assert factorial(5) == 120
assert factorial(6) == 720
assert factorial(10) == 3628800

# Larger value
assert factorial(12) == 479001600

# Negative input must raise ValueError
try:
    factorial(-1)
    raise AssertionError("Expected ValueError for factorial(-1)")
except ValueError:
    pass

try:
    factorial(-10)
    raise AssertionError("Expected ValueError for factorial(-10)")
except ValueError:
    pass

print("All test cases passed.")

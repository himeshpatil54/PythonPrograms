"""Test file for 01_even_odd.py"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Test_Code._import_helper import load_module

mod = load_module("Code/01_even_odd.py")
is_even = mod.is_even

# Normal even numbers
assert is_even(2) is True
assert is_even(10) is True
assert is_even(100) is True

# Normal odd numbers
assert is_even(1) is False
assert is_even(7) is False
assert is_even(99) is False

# Boundary: zero is even
assert is_even(0) is True

# Negative even
assert is_even(-4) is True
assert is_even(-2) is True

# Negative odd
assert is_even(-3) is False
assert is_even(-7) is False

print("All test cases passed.")

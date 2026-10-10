"""Test file for 10_sum_of_digits.py"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Test_Code._import_helper import load_module

mod = load_module("Code/10_sum_of_digits.py")
sum_of_digits = mod.sum_of_digits

# Normal positive
assert sum_of_digits(1234) == 10
assert sum_of_digits(9999) == 36
assert sum_of_digits(100) == 1

# Zero
assert sum_of_digits(0) == 0

# Negative (sign ignored)
assert sum_of_digits(-567) == 18
assert sum_of_digits(-1234) == 10

# Single digit
assert sum_of_digits(5) == 5
assert sum_of_digits(9) == 9

# Larger number
assert sum_of_digits(99999) == 45

print("All test cases passed.")

"""Test file for 08_reverse_number.py"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Test_Code._import_helper import load_module

mod = load_module("Code/08_reverse_number.py")
reverse_number = mod.reverse_number

# Normal positive
assert reverse_number(1234) == 4321
assert reverse_number(9876) == 6789
assert reverse_number(12) == 21

# Negative numbers (sign preserved)
assert reverse_number(-567) == -765
assert reverse_number(-1234) == -4321

# Trailing zeros become leading zeros (dropped)
assert reverse_number(100) == 1
assert reverse_number(1000) == 1
assert reverse_number(120) == 21

# Single digit
assert reverse_number(5) == 5
assert reverse_number(0) == 0

# Palindrome number
assert reverse_number(121) == 121

print("All test cases passed.")

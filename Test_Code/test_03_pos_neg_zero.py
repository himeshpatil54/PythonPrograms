"""Test file for 03_pos_neg_zero.py"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Test_Code._import_helper import load_module

mod = load_module("Code/03_pos_neg_zero.py")
classify_number = mod.classify_number

# Positive numbers
assert classify_number(1) == "Positive"
assert classify_number(100) == "Positive"
assert classify_number(0.1) == "Positive"

# Negative numbers
assert classify_number(-1) == "Negative"
assert classify_number(-100) == "Negative"
assert classify_number(-0.5) == "Negative"

# Zero
assert classify_number(0) == "Zero"

# Boundary: very large and very small
assert classify_number(1e10) == "Positive"
assert classify_number(-1e10) == "Negative"

print("All test cases passed.")

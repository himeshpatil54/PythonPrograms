"""Test file for 07_primes_in_range.py"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Test_Code._import_helper import load_module

mod = load_module("Code/07_primes_in_range.py")
primes_in_range = mod.primes_in_range

# Normal range
assert primes_in_range(1, 20) == [2, 3, 5, 7, 11, 13, 17, 19]
assert primes_in_range(10, 30) == [11, 13, 17, 19, 23, 29]

# Range with no primes
assert primes_in_range(14, 16) == []
assert primes_in_range(24, 28) == []

# Single prime endpoint
assert primes_in_range(2, 2) == [2]
assert primes_in_range(7, 7) == [7]

# Single non-prime endpoint
assert primes_in_range(4, 4) == []

# Range starting at 0
assert primes_in_range(0, 10) == [2, 3, 5, 7]

# Negative start
assert primes_in_range(-5, 5) == [2, 3, 5]

print("All test cases passed.")

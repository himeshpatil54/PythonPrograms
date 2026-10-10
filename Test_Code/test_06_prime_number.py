"""Test file for 06_prime_number.py"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Test_Code._import_helper import load_module

mod = load_module("Code/06_prime_number.py")
is_prime = mod.is_prime

# Below 2 — always False
assert is_prime(0) is False
assert is_prime(1) is False
assert is_prime(-5) is False
assert is_prime(-1) is False

# Boundary prime
assert is_prime(2) is True
assert is_prime(3) is True

# Known primes
assert is_prime(5) is True
assert is_prime(7) is True
assert is_prime(11) is True
assert is_prime(13) is True
assert is_prime(17) is True
assert is_prime(19) is True
assert is_prime(97) is True

# Known composites
assert is_prime(4) is False
assert is_prime(6) is False
assert is_prime(9) is False
assert is_prime(15) is False
assert is_prime(100) is False

print("All test cases passed.")

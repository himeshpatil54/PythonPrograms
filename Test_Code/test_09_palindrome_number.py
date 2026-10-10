"""Test file for 09_palindrome_number.py"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Test_Code._import_helper import load_module

mod = load_module("Code/09_palindrome_number.py")
is_palindrome_number = mod.is_palindrome_number

# True palindromes
assert is_palindrome_number(121) is True
assert is_palindrome_number(1221) is True
assert is_palindrome_number(12321) is True
assert is_palindrome_number(0) is True
assert is_palindrome_number(7) is True
assert is_palindrome_number(11) is True

# Non-palindromes
assert is_palindrome_number(123) is False
assert is_palindrome_number(10) is False
assert is_palindrome_number(100) is False

# Negative — always False
assert is_palindrome_number(-121) is False
assert is_palindrome_number(-1) is False

print("All test cases passed.")

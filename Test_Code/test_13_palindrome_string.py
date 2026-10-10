"""Test file for 13_palindrome_string.py"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Test_Code._import_helper import load_module

mod = load_module("Code/13_palindrome_string.py")
is_palindrome_string = mod.is_palindrome_string

# Simple palindromes
assert is_palindrome_string("racecar") is True
assert is_palindrome_string("madam") is True
assert is_palindrome_string("level") is True

# Case-insensitive
assert is_palindrome_string("Racecar") is True
assert is_palindrome_string("MadAm") is True

# With spaces and punctuation
assert is_palindrome_string("A man a plan a canal Panama") is True
assert is_palindrome_string("Was it a car or a cat I saw?") is True
assert is_palindrome_string("Never odd or even") is True

# Non-palindromes
assert is_palindrome_string("hello") is False
assert is_palindrome_string("Python") is False

# Empty string (trivially palindrome)
assert is_palindrome_string("") is True

# Single character
assert is_palindrome_string("a") is True

# Numbers retained
assert is_palindrome_string("12321") is True
assert is_palindrome_string("12345") is False

print("All test cases passed.")

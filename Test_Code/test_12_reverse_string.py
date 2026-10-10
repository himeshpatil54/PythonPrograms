"""Test file for 12_reverse_string.py"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Test_Code._import_helper import load_module

mod = load_module("Code/12_reverse_string.py")
reverse_string = mod.reverse_string

# Normal strings
assert reverse_string("hello") == "olleh"
assert reverse_string("Python") == "nohtyP"
assert reverse_string("abcde") == "edcba"

# Empty string
assert reverse_string("") == ""

# Single character
assert reverse_string("a") == "a"

# Palindrome (same reversed)
assert reverse_string("racecar") == "racecar"

# With spaces and punctuation
assert reverse_string("Hello World!") == "!dlroW olleH"

# Numbers as string
assert reverse_string("12345") == "54321"

# Mixed case
assert reverse_string("AbCd") == "dCbA"

print("All test cases passed.")

"""Test file for 11_vowels_consonants.py"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Test_Code._import_helper import load_module

mod = load_module("Code/11_vowels_consonants.py")
count_vowels_consonants = mod.count_vowels_consonants

# Normal sentence
assert count_vowels_consonants("Hello World") == (3, 7)

# All vowels
assert count_vowels_consonants("aeiou") == (5, 0)
assert count_vowels_consonants("AEIOU") == (5, 0)

# All consonants
assert count_vowels_consonants("bcdf") == (0, 4)

# Mixed case
assert count_vowels_consonants("Python") == (1, 5)

# With digits, spaces, punctuation (ignored)
assert count_vowels_consonants("Hello 123!") == (2, 3)

# Empty string
assert count_vowels_consonants("") == (0, 0)

# Only spaces and digits
assert count_vowels_consonants("  123  ") == (0, 0)

# Uppercase and lowercase counted equally
assert count_vowels_consonants("AaBbEe") == (4, 2)

print("All test cases passed.")

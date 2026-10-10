"""Test file for 14_char_frequency.py"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Test_Code._import_helper import load_module

mod = load_module("Code/14_char_frequency.py")
character_frequency = mod.character_frequency

# Empty string
assert character_frequency("") == {}

# Single character
assert character_frequency("a") == {"a": 1}

# All same characters
assert character_frequency("aaa") == {"a": 3}

# Mixed with case preserved
assert character_frequency("aA") == {"a": 1, "A": 1}

# Common word
result = character_frequency("hello")
assert result == {"h": 1, "e": 1, "l": 2, "o": 1}

# Spaces and punctuation counted
result = character_frequency("hi!")
assert result == {"h": 1, "i": 1, "!": 1}

# Space counted
result = character_frequency("a b")
assert result == {"a": 1, " ": 1, "b": 1}

# Numbers counted
result = character_frequency("a1a")
assert result == {"a": 2, "1": 1}

print("All test cases passed.")

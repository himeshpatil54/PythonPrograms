"""Test file for 20_word_frequency.py"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Test_Code._import_helper import load_module

mod = load_module("Code/20_word_frequency.py")
word_frequency = mod.word_frequency

# Assignment example
assert word_frequency("Hello, hello world!") == {"hello": 2, "world": 1}

# Case-insensitive
assert word_frequency("The the THE") == {"the": 3}

# Punctuation stripped around words
assert word_frequency("cat, cat. cat!") == {"cat": 3}

# Multiple distinct words
result = word_frequency("one two three two one")
assert result == {"one": 2, "two": 2, "three": 1}

# Empty string
assert word_frequency("") == {}

# Whitespace only
assert word_frequency("   ") == {}

# Single word
assert word_frequency("hello") == {"hello": 1}

# Numbers in sentence treated as words
assert word_frequency("1 2 1") == {"1": 2, "2": 1}

# Mixed punctuation
result = word_frequency("Well... well, well!")
assert result == {"well": 3}

print("All test cases passed.")

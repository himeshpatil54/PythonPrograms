# PythonPrograms

A collection of 20 beginner-friendly Python programs with matching test files.

**Assignment Deadline:** Monday, 5 October 2026

---

## Folder Structure

```
PythonPrograms/
├── Code/                   # 20 Python implementation files
│   ├── 01_even_odd.py
│   ├── 02_largest_of_three.py
│   ├── 03_pos_neg_zero.py
│   ├── 04_factorial.py
│   ├── 05_fibonacci_series.py
│   ├── 06_prime_number.py
│   ├── 07_primes_in_range.py
│   ├── 08_reverse_number.py
│   ├── 09_palindrome_number.py
│   ├── 10_sum_of_digits.py
│   ├── 11_vowels_consonants.py
│   ├── 12_reverse_string.py
│   ├── 13_palindrome_string.py
│   ├── 14_char_frequency.py
│   ├── 15_second_largest.py
│   ├── 16_remove_duplicates.py
│   ├── 17_common_elements.py
│   ├── 18_missing_number.py
│   ├── 19_find_duplicates.py
│   └── 20_word_frequency.py
└── Test_Code/              # 20 matching test files
    ├── _import_helper.py   # Utility: loads numeric-named modules
    ├── test_01_even_odd.py
    ├── test_02_largest_of_three.py
    ├── test_03_pos_neg_zero.py
    ├── test_04_factorial.py
    ├── test_05_fibonacci_series.py
    ├── test_06_prime_number.py
    ├── test_07_primes_in_range.py
    ├── test_08_reverse_number.py
    ├── test_09_palindrome_number.py
    ├── test_10_sum_of_digits.py
    ├── test_11_vowels_consonants.py
    ├── test_12_reverse_string.py
    ├── test_13_palindrome_string.py
    ├── test_14_char_frequency.py
    ├── test_15_second_largest.py
    ├── test_16_remove_duplicates.py
    ├── test_17_common_elements.py
    ├── test_18_missing_number.py
    ├── test_19_find_duplicates.py
    └── test_20_word_frequency.py
```

---

## Programs Summary

| # | Program | Function | Description |
|---|---------|----------|-------------|
| 01 | Even or Odd | `is_even(n)` | Returns True if n is even |
| 02 | Largest of Three | `largest_of_three(a,b,c)` | Returns the largest value |
| 03 | Positive/Negative/Zero | `classify_number(n)` | Classifies a number |
| 04 | Factorial | `factorial(n)` | Computes n! |
| 05 | Fibonacci Series | `fibonacci_series(n)` | First n Fibonacci numbers |
| 06 | Prime Number | `is_prime(n)` | Checks if n is prime |
| 07 | Primes in Range | `primes_in_range(start, end)` | All primes in [start, end] |
| 08 | Reverse Number | `reverse_number(n)` | Reverses digits of n |
| 09 | Palindrome Number | `is_palindrome_number(n)` | Checks if n reads same backward |
| 10 | Sum of Digits | `sum_of_digits(n)` | Sum of all digits of n |
| 11 | Vowels & Consonants | `count_vowels_consonants(text)` | Returns (vowels, consonants) |
| 12 | Reverse String | `reverse_string(text)` | Reverses a string using a loop |
| 13 | Palindrome String | `is_palindrome_string(text)` | Checks if string is palindrome |
| 14 | Character Frequency | `character_frequency(text)` | Dict of character counts |
| 15 | Second Largest | `second_largest(numbers)` | Second-largest distinct value |
| 16 | Remove Duplicates | `remove_duplicates(items)` | Removes duplicates, keeps order |
| 17 | Common Elements | `common_elements(l1, l2)` | Elements common to both lists |
| 18 | Missing Number | `find_missing_number(numbers)` | Finds missing int in 0..n range |
| 19 | Find Duplicates | `find_duplicates(items)` | Returns duplicate values once |
| 20 | Word Frequency | `word_frequency(sentence)` | Dict of word frequencies |

---

## How to Run Tests

Run **all** test files from the **repository root** (`PythonPrograms/`):

```bash
python Test_Code/test_01_even_odd.py
python Test_Code/test_02_largest_of_three.py
python Test_Code/test_03_pos_neg_zero.py
python Test_Code/test_04_factorial.py
python Test_Code/test_05_fibonacci_series.py
python Test_Code/test_06_prime_number.py
python Test_Code/test_07_primes_in_range.py
python Test_Code/test_08_reverse_number.py
python Test_Code/test_09_palindrome_number.py
python Test_Code/test_10_sum_of_digits.py
python Test_Code/test_11_vowels_consonants.py
python Test_Code/test_12_reverse_string.py
python Test_Code/test_13_palindrome_string.py
python Test_Code/test_14_char_frequency.py
python Test_Code/test_15_second_largest.py
python Test_Code/test_16_remove_duplicates.py
python Test_Code/test_17_common_elements.py
python Test_Code/test_18_missing_number.py
python Test_Code/test_19_find_duplicates.py
python Test_Code/test_20_word_frequency.py
```

Each test prints `All test cases passed.` on success.

You can also compile-check all files at once:

```bash
python -m compileall -q Code Test_Code
```

If pytest is installed:

```bash
pytest Test_Code/ -v
```

> **Note:** Tests must be run from the `PythonPrograms/` root directory so that import paths resolve correctly.

---

## Git Workflow (One File at a Time)

Each of the 40 assignment files was committed and pushed **individually** in this order:

1. Program file → `git add Code/<file>.py` → commit → push
2. Test file → `git add Test_Code/test_<file>.py` → commit → push
3. Repeat for all 20 programs

Example for Program 1:
```bash
git add Code/01_even_odd.py
git commit -m "Add even odd program"
git push origin main

git add Test_Code/test_01_even_odd.py
git commit -m "Add even odd test cases"
git push origin main
```

---

## Requirements

- Python 3.6+
- No external dependencies (standard library only)

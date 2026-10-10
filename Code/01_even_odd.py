"""
Program 1: Even or Odd
Determine whether a given integer is even or odd.
"""


def is_even(number):
    """Return True if number is even, False if odd."""
    return number % 2 == 0


if __name__ == "__main__":
    print(is_even(4))   # True
    print(is_even(7))   # False
    print(is_even(0))   # True

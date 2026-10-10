"""
Program 9: Palindrome Number
Check whether a non-negative integer reads the same backward.
"""


def is_palindrome_number(n):
    """
    Return True if n is a non-negative palindrome integer, False otherwise.
    Negative integers always return False.
    """
    if n < 0:
        return False
    s = str(n)
    return s == s[::-1]


if __name__ == "__main__":
    print(is_palindrome_number(121))   # True
    print(is_palindrome_number(123))   # False
    print(is_palindrome_number(-121))  # False
    print(is_palindrome_number(0))     # True

"""
Program 13: Palindrome String
Check whether a string is a palindrome (ignoring spaces, punctuation, case).
"""
import re


def is_palindrome_string(text):
    """
    Return True if text is a palindrome.
    Ignores spaces and punctuation.
    Comparison is case-insensitive.
    Only letters and digits are considered.
    """
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", text).lower()
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    print(is_palindrome_string("racecar"))              # True
    print(is_palindrome_string("A man a plan a canal Panama"))  # True
    print(is_palindrome_string("hello"))                # False
    print(is_palindrome_string("Was it a car or a cat I saw?"))  # True

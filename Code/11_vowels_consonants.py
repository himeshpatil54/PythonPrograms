"""
Program 11: Count Vowels and Consonants
Count the number of vowels and consonants in a string.
"""


def count_vowels_consonants(text):
    """
    Return a tuple (vowels, consonants).
    Counts only English alphabetic characters.
    Ignores numbers, spaces, and punctuation.
    Case-insensitive.
    """
    vowels_set = set("aeiou")
    vowels = 0
    consonants = 0
    for ch in text.lower():
        if ch.isalpha():
            if ch in vowels_set:
                vowels += 1
            else:
                consonants += 1
    return (vowels, consonants)


if __name__ == "__main__":
    print(count_vowels_consonants("Hello World"))  # (3, 7)
    print(count_vowels_consonants("Python 3!"))    # (1, 5)
    print(count_vowels_consonants(""))             # (0, 0)

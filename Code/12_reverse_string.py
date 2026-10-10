"""
Program 12: Reverse a String Without Slicing
Reverse a string using a loop (no negative-step slicing).
"""


def reverse_string(text):
    """
    Return the reverse of text.
    Uses a loop — does NOT use negative-step slicing ([::-1]).
    """
    result = []
    for ch in text:
        result.insert(0, ch)
    return "".join(result)


if __name__ == "__main__":
    print(reverse_string("hello"))   # "olleh"
    print(reverse_string("Python"))  # "nohtyP"
    print(reverse_string(""))        # ""
    print(reverse_string("a"))       # "a"

"""
Program 20: Word Frequency
Count the frequency of each word in a sentence.

Tokenization: words are extracted by stripping surrounding punctuation from
whitespace-separated tokens, then lowercased.
Example: "Hello, hello world!" -> {"hello": 2, "world": 1}
"""
import re


def word_frequency(sentence):
    """
    Return a dictionary mapping each word (lowercased) to its frequency.
    Punctuation surrounding words is ignored.
    Returns {} for an empty or whitespace-only sentence.
    """
    if not sentence or not sentence.strip():
        return {}
    words = re.findall(r"[a-zA-Z0-9]+", sentence.lower())
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


if __name__ == "__main__":
    print(word_frequency("Hello, hello world!"))        # {'hello': 2, 'world': 1}
    print(word_frequency("The cat sat on the mat."))    # {'the': 2, 'cat': 1, ...}
    print(word_frequency(""))                           # {}
    print(word_frequency("   "))                        # {}

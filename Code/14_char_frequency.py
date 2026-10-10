"""
Program 14: Character Frequency
Count the frequency of each character in a string.
"""


def character_frequency(text):
    """
    Return a dictionary mapping each character to its count in text.
    Preserves original case.
    Counts spaces and punctuation.
    Returns {} for an empty string.
    """
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


if __name__ == "__main__":
    print(character_frequency("hello"))   # {'h':1,'e':1,'l':2,'o':1}
    print(character_frequency(""))        # {}
    print(character_frequency("aA"))      # {'a':1,'A':1}

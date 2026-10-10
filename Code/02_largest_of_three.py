"""
Program 2: Largest of Three Numbers
Find the largest among three given numbers.
"""


def largest_of_three(a, b, c):
    """Return the largest value among a, b, and c. Handles ties correctly."""
    return max(a, b, c)


if __name__ == "__main__":
    print(largest_of_three(3, 7, 5))   # 7
    print(largest_of_three(10, 10, 5)) # 10
    print(largest_of_three(-1, -2, -3))# -1

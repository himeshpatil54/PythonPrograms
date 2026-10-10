"""
Program 10: Sum of Digits
Calculate the sum of all decimal digits of an integer.
"""


def sum_of_digits(n):
    """
    Return the sum of the decimal digits of n.
    Ignores the sign for negative integers.
    Returns 0 for zero.
    """
    return sum(int(d) for d in str(abs(n)))


if __name__ == "__main__":
    print(sum_of_digits(1234))   # 10
    print(sum_of_digits(-567))   # 18
    print(sum_of_digits(0))      # 0

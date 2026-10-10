"""
Program 8: Reverse a Number
Reverse the decimal digits of an integer, preserving sign.
"""


def reverse_number(n):
    """
    Reverse the decimal digits of n.
    Preserves the sign of negative integers.
    Leading zeros in the result are dropped (standard integer behavior).
    """
    sign = -1 if n < 0 else 1
    reversed_digits = int(str(abs(n))[::-1])
    return sign * reversed_digits


if __name__ == "__main__":
    print(reverse_number(1234))   # 4321
    print(reverse_number(-567))   # -765
    print(reverse_number(100))    # 1  (leading zeros dropped)
    print(reverse_number(0))      # 0

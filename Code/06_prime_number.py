"""
Program 6: Prime Number
Check whether a given integer is a prime number.
"""


def is_prime(n):
    """
    Return True if n is a prime number, False otherwise.
    Returns False for integers below 2.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


if __name__ == "__main__":
    print(is_prime(2))   # True
    print(is_prime(17))  # True
    print(is_prime(18))  # False
    print(is_prime(1))   # False

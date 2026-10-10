"""
Program 7: Primes in a Range
Find all prime numbers within a given inclusive range.
"""


def primes_in_range(start, end):
    """
    Return a sorted list of all prime numbers between start and end (inclusive).
    Returns an empty list if no primes exist in the range.
    """
    def is_prime(n):
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

    return [n for n in range(start, end + 1) if is_prime(n)]


if __name__ == "__main__":
    print(primes_in_range(1, 20))   # [2, 3, 5, 7, 11, 13, 17, 19]
    print(primes_in_range(14, 16))  # []
    print(primes_in_range(2, 2))    # [2]

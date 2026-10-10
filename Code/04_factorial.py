"""
Program 4: Factorial
Calculate the factorial of a non-negative integer.
"""


def factorial(n):
    """
    Return the factorial of n.
    Returns 1 for n == 0.
    Raises ValueError for negative integers.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print(factorial(0))  # 1
    print(factorial(5))  # 120
    print(factorial(10)) # 3628800

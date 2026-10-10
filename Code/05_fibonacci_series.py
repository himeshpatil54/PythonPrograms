"""
Program 5: Fibonacci Series
Generate the first n Fibonacci numbers.
"""


def fibonacci_series(n):
    """
    Return a list containing the first n Fibonacci numbers starting with 0, 1.
    Returns [] when n == 0.
    Raises ValueError when n < 0.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    if n == 0:
        return []
    series = [0]
    if n == 1:
        return series
    series.append(1)
    for i in range(2, n):
        series.append(series[-1] + series[-2])
    return series


if __name__ == "__main__":
    print(fibonacci_series(0))  # []
    print(fibonacci_series(1))  # [0]
    print(fibonacci_series(8))  # [0, 1, 1, 2, 3, 5, 8, 13]

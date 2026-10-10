"""
Program 18: Find Missing Number
Find the one missing number from a list representing the range 0..n with one gap.
"""


def find_missing_number(numbers):
    """
    Accept a list of distinct integers representing the range 0 through n
    with exactly one missing value. Return the missing value.

    Raises ValueError for:
    - Empty list
    - Duplicate values
    - Values out of expected range
    - List already containing all values (no missing number)
    """
    if not numbers:
        raise ValueError("Input list must not be empty.")

    # The list should have n elements for range 0..n (n+1 values, 1 missing => n elements)
    n = len(numbers)  # Expected range is 0..n, so n+1 values, one missing
    expected_sum = n * (n + 1) // 2

    # Validate: no duplicates and all values in [0, n]
    if len(set(numbers)) != len(numbers):
        raise ValueError("Input contains duplicate values.")
    for val in numbers:
        if val < 0 or val > n:
            raise ValueError(f"Value {val} is out of the expected range [0, {n}].")

    return expected_sum - sum(numbers)


if __name__ == "__main__":
    print(find_missing_number([1, 2, 3, 4, 5]))   # 0 (missing from start)
    print(find_missing_number([0, 1, 3, 4, 5]))   # 2 (missing from middle)
    print(find_missing_number([0, 1, 2, 3, 4]))   # 5 (missing from end)

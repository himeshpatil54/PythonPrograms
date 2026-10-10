"""
Program 15: Second Largest Number
Find the second-largest distinct value in a list of numbers.
"""


def second_largest(numbers):
    """
    Return the second-largest DISTINCT value in the list.
    Raises ValueError if fewer than two distinct values exist.
    """
    distinct = list(set(numbers))
    if len(distinct) < 2:
        raise ValueError("Need at least two distinct values to find the second largest.")
    distinct.sort(reverse=True)
    return distinct[1]


if __name__ == "__main__":
    print(second_largest([3, 1, 4, 1, 5, 9, 2, 6]))  # 6
    print(second_largest([10, 10, 9]))                 # 9
    print(second_largest([1, 2]))                      # 1

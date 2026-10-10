"""
Program 16: Remove Duplicates
Remove duplicate elements from a list while preserving original order.
"""


def remove_duplicates(items):
    """
    Return a new list with duplicates removed, preserving the original order.
    Assumes items are hashable.
    """
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


if __name__ == "__main__":
    print(remove_duplicates([1, 2, 3, 2, 1, 4]))       # [1, 2, 3, 4]
    print(remove_duplicates(["a", "b", "a", "c"]))     # ['a', 'b', 'c']
    print(remove_duplicates([]))                        # []

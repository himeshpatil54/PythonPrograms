"""
Program 19: Find Duplicate Elements
Identify elements that appear more than once in a list.
"""


def find_duplicates(items):
    """
    Return a list of elements that appear more than once in items.
    Each duplicated value is returned only once.
    Preserves the order in which values first become duplicates
    (i.e., the order of second occurrence).
    """
    seen = set()
    duplicates = []
    reported = set()
    for item in items:
        if item in seen and item not in reported:
            duplicates.append(item)
            reported.add(item)
        seen.add(item)
    return duplicates


if __name__ == "__main__":
    print(find_duplicates([1, 2, 3, 2, 4, 3, 5]))  # [2, 3]
    print(find_duplicates([1, 1, 1, 1]))            # [1]
    print(find_duplicates([1, 2, 3]))               # []
    print(find_duplicates([]))                       # []

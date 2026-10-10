"""
Program 17: Common Elements
Find elements common to two lists, preserving order of first appearance in list1.
"""


def common_elements(list1, list2):
    """
    Return a list of distinct elements present in both list1 and list2.
    Order follows the first appearance in list1.
    """
    set2 = set(list2)
    seen = set()
    result = []
    for item in list1:
        if item in set2 and item not in seen:
            seen.add(item)
            result.append(item)
    return result


if __name__ == "__main__":
    print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))   # [3, 4]
    print(common_elements([1, 2, 2, 3], [2, 3, 4]))       # [2, 3]
    print(common_elements([], [1, 2]))                     # []
    print(common_elements([1, 2], []))                     # []

from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity:O(n*m*k) because we are iterating through both lists and then checking if the item is already in the common items list
    Space Complexity:O(n) because we are storing the common items in a new list
    Optimal time complexity: O(n+m) because we have to iterate through both lists at least once to find the common items
    """
    # common_items: List[ItemType] = []
    # for i in first_sequence:
    #     for j in second_sequence:
    #         if i == j and i not in common_items:
    #             common_items.append(i)
    # return common_items


    first_set = set(first_sequence)
    second_set = set(second_sequence)
    return list(first_set & second_set)

    """
    Time Complexity now: O(n+m) because we are iterating through both list once
    Space Complexity now: O(n+m) because we are storing the common items in a new list and we are also creating two sets which take up space
    Optimal time complexity: O(n+m) because we have to iterate through both lists at least once to find the common items
    """



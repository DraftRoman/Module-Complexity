from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    # for value in values:
    #     is_duplicate = False
    #     for existing in unique_items:
    #         if value == existing:
    #             is_duplicate = True
    #             break
    #     if not is_duplicate:
    #         unique_items.append(value)

    # return unique_items
    
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

    Time complexity: O(n^2) we are iterating for each item in the list and then we're doing another iteration th check duplicates
    Space complexity: O(n) creating a new list 
    Optimal time complexity: O(n) we can use set to check  for duplicates 
    """
    
    unique_items: list[ItemType] = []
    seen = set()

    for value in values:
        if value not in seen:
            seen.add(value)
            unique_items.append(value)
    return unique_items


    



    # unique_items = list(set(values))
    
    # return unique_items
"""

Time: O(n)
Space: O(n)

"""


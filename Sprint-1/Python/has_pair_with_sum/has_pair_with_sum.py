from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity: O(n^2) because we are iterating through the list twice to find the pair of numbers that sum to the target value
    Space Complexity: O(1) because we are not using any extra space
    Optimal time complexity: O(n) because we can use a hash set to store the numbers we have seen so far
    """
    # for i in range(len(numbers)):
    #     for j in range(i + 1, len(numbers)):
    #         if numbers[i] + numbers[j] == target_sum:
    #             return True
    # return False
    for num in numbers:
        complement = target_sum - num
        if complement in numbers:
            return True
    return False

"""
Time Comlexity now: O(n) because we are iterating once through the list to find the pair
Scape Complexity now: O(n) because we aren't using any extra space, we ca have some list for saving the numbers, but we don't need it here
"""

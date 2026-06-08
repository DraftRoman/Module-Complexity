from typing import Dict, List


def calculate_sum_and_product(input_numbers: List[int]) -> Dict[str, int]:
    """
    Calculate the sum and product of integers in a list.

    Note: the sum is every number added together
    and the product is every number multiplied together
    so for example: [2, 3, 5] would return
    {
        "sum": 10, // 2 + 3 + 5
        "product": 30 // 2 * 3 * 5
    }
    Time Complexity: O(n) because we are iterating through the list once now instead of twice before
    Space Complexity: O(1) because we are using a constant amount of space
    Optimal time complexity:
    We can calculate the sum and the product in a single pass through the list
    """
    # Edge case: empty list
    if not input_numbers:
        return {"sum": 0, "product": 1}

    total = 0     
    product = 1

    for current_number in input_numbers:
        product *= current_number
        total += current_number

    return {"sum": total, "product": product}

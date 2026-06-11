from functools import lru_cache
from typing import List

def find_longest_common_prefix(strings: List[str]) -> str:
    if len(strings) < 2:
        return ""

    sorted_strings = sorted(strings)
    longest = ""

    for i in range(len(sorted_strings) - 1):
            common = find_common_prefix(sorted_strings[i], sorted_strings[i + 1])
            if len(common) > len(longest):
                longest = common
    return longest

@lru_cache(maxsize=None)
def find_common_prefix(left: str, right: str) -> str:
    i = 0
    limit = min(len(left), len(right))

    while i < limit and left[i] == right[i]:
        i += 1

    return left[:i]
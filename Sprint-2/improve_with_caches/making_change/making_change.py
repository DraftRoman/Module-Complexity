from functools import lru_cache
from coin import Coin

COINS = [
    Coin("200 coins", 200),
    Coin("100 coins", 100),
    Coin("50 coins", 50),
    Coin("20 coins", 20),
    Coin("10 coins", 10),
    Coin("5 coins", 5),
    Coin("2 coins", 2),
    Coin("1 coin", 1),
]


def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values 1, 2, 5, 10, 20, 50, 100, 200,
    returns the number of ways to make the total.
    """
    @lru_cache(maxsize=None)
    def helper(remaining: int, index: int) -> int:
        
        if remaining == 0:
            return 1
        
        if index == len(COINS):
            return 0

        ways = 0
        coin = COINS[index]

        max_count = remaining 

        for count in range(max_count + 1):
            new_remaining = remaining - count * coin.value
            ways += helper(new_remaining, index + 1)

        return ways

    return helper(total, 0)
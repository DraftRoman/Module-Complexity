from typing import List
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
    return ways_to_make_change_helper(total, COINS)


def ways_to_make_change_helper(total: int, coins: List[Coin]) -> int:
    
    if total == 0:
        return 1


    if len(coins) == 0:
        return 0

    ways = 0

    for coin_index in range(len(coins)):
        coin = coins[coin_index]
        count_of_coin = 1

        while coin.value * count_of_coin <= total:
            total_from_coins = coin.value * count_of_coin

            if total_from_coins == total:
                ways += 1
            else:
                ways += ways_to_make_change_helper(
                    total - total_from_coins,
                    coins[coin_index + 1:]
                )

            count_of_coin += 1

    return ways
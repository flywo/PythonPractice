#!/usr/bin/env python
# coding:utf-8

def check(price, den):
    coins_need = [0 for _ in range(min(den))]
    for money in range(min(den), price+1):
        min_coins = money
        for coin in [d for d in den if d <= money]:
            if coins_need[money-coin]==0 and money not in den:
                min_coins = 0
                break
            else:
                min_coins = min(min_coins, coins_need[money-coin]+1)
        coins_need.append(min_coins)
    return coins_need[-1] if coins_need[-1] else None


def check1(price, denoms):
    sums = set()
    for number in range(1, price+1):
        sums = {s+d for s in sums for d in denoms} or set(denoms)
        if price in sums:
            return number


if __name__ == '__main__':
    assert check(11, [1, 4, 5]) == 3
    print(check1(13, [1, 2, 5]))

    res = {1,} or {1,3,6}
    pass
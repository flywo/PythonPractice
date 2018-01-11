#!/usr/bin/env python
# coding:utf-8

import random

def check(price, denominations):
    arr = sorted(denominations, reverse=True)
    if price < min(arr):
        return None
    def fun(x, y, up):
        if arr.index(x)==len(arr)-1 and y%x!=0:
            return None
        return y//x+up if y%x==0 else \
            fun(arr[arr.index(x)+1], y%x, up+y//x)
    res = [fun(x, price, 0) for x in arr]
    return min(res) if None not in res else None

if __name__ == '__main__':
    arr = (123456, [1,6,7,456,678])
    print(check(*arr))
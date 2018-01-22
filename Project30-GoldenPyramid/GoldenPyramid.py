#!/usr/bin/env python
# coding:utf-8

def check(pyramid):
    gold = list(pyramid[-1])
    for row in pyramid[-2::-1]:
        for i, val in enumerate(row):
            gold[i] = val + max(gold[i], gold[i+1])
        gold.pop()
    return gold[0]


def check1(pyramid):
    py = [list(i) for i in pyramid]
    for i in reversed(range(len(py)-1)):
        for j in range(i+1):
            py[i][j]+=max(py[i+1][j], py[i+1][j+1])
    return py[0][0]


from functools import reduce
def sum_triangle(top, left, right):
    return top+max(left, right)
def integrate(lowerline, upperline):
    return list(map(sum_triangle, upperline, lowerline, lowerline[1:]))
def count_gold(pyramid):
    result = reduce(integrate, reversed(pyramid))
    return result.pop()


def count_gold2(pyramid):
    p = tuple(map(list, pyramid))
    for i in reversed(range(len(p))):
        for j in range(i): p[i-1][j] += max(p[i][j:j+2])
    return p[0][0]


if __name__ == '__main__':
    arr = (
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )
    print(check(arr))
    print(check1(arr))
    print(count_gold(arr))
    print(count_gold2(arr))


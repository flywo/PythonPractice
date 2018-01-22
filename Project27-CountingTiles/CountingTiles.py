#!/usr/bin/env python
# coding:utf-8

from math import ceil, hypot


#计算距离
def getMaxAndMinDistances(radius):
    radius = int(ceil(radius))
    distances = []
    for row in range(radius):
        for col in range(radius):
            temp = [hypot(row - radius, col - radius), hypot(row - radius, radius - col - 1),
                    hypot(radius - row - 1, radius - col), hypot(radius - row - 1, radius - col - 1)]
            distances.append((min(temp), max(temp)))
    return distances


def checkio(radius):
    distances = getMaxAndMinDistances(radius)
    #过滤掉不符合的元素
    solid = len(list(filter(lambda x: x[1] < radius, distances)))
    partial = len(list(filter(lambda x: x[1] > radius > x[0], distances)))
    #上面只计算了一个象限，*4既是所有的结果
    return [solid * 4, partial * 4]


def check2(radius):
    ran, solid, total = range(int(radius)+1),0,0
    for x in ran:
        for y in ran:
            #1j表示复数
            solid+=abs(x+y*1j+1+1j)<=radius
            total+=abs(x+y*1j)<radius
    return [solid*4,(total-solid)*4]


# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio(2) == [4, 12], "N=2"
    assert checkio(3) == [16, 20], "N=3"
    assert checkio(2.1) == [4, 20], "N=2.1"
    assert check2(2.5) == [12, 20], "N=2.5"

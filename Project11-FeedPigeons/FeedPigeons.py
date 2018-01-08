#!/usr/bin/env python
# coding:utf-8

import itertools

def check(number):

    def getSu(number):
        sum = 0
        for x in range(1, number+1):
            sum += (number+1-x)*x
        return sum

    x = 1
    last = 0
    while True:
        getsum = getSu(x)
        if getsum>=number:
            su = getsum-x
            for n in range(x+1):
                if su+n == number:
                    last = n
                    break
            break
        x += 1
    return sum([number for number in range(x)])+last

#大神解法
def check1(food):
    pigeons = 0
    for t in itertools.count(1):
        if pigeons+t > food:
            return max(pigeons, food)
        pigeons += t
        food -= pigeons

def check2(food):
    birds = new = 0
    while food > 0:
        new += 1
        birds += new
        food -= birds
    return birds + max(food, -new)

if __name__ == '__main__':
    print(check(9))
    print(check1(9))

    f = lambda n,y=0,i=0:n<y and max(n,y-i+1) or f(n-y,sum(range(i+1)), i+1)
    print(f(9))

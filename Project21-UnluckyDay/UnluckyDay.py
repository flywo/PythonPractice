#!/usr/bin/env python
# coding:utf-8

import calendar

def check(year):
    return len([1 for x in range(1, 13) if calendar.weekday(year, x, 13)==4])

def check1(year):
    return sum(calendar.weekday(year, month, 13)==calendar.FRIDAY for month in range(1, 13))



if __name__ == '__main__':
    print(check(2015))
    print(check1(2015))

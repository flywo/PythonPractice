#!/usr/bin/env python
# coding:utf-8

WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

import calendar
import itertools
from calendar import day_name, isleap, weekday

def check(year):
    years = list(itertools.repeat(year, 7))
    first_m = list(itertools.repeat(1, 7))
    end_m = list(itertools.repeat(12, 7))
    first_d = range(1, 8)
    end_d = range(25, 32)
    begin = list(map(calendar.weekday, years, first_m, first_d))
    end = list(map(calendar.weekday, years, end_m, end_d))
    begin = set(begin[:begin.index(0)])
    end = set(end[end.index(0):])
    if begin.isdisjoint(end):
        res = sorted(begin | end)
    else:
        res = sorted(begin & end)
    return [WEEK[x] for x in res]


#大神，由于每年只有365天或者366天，所以，只需要判断开头的两天或者一天的日期，即可知道星期几是最多的
def check1(year):
    days = (weekday(year, 1, 1+i) for i in range(1+isleap(year)))
    return [day_name[d] for d in sorted(days)]

#判断开头和结尾的两天即可
def check2(year):
    days = {calendar.weekday(year, 1, 1), calendar.weekday(year, 12, 31)}
    return [calendar.day_name[i] for i in sorted(days)]

if __name__ == '__main__':
    print(check(328))
    print(check(328))
    print(check(328))

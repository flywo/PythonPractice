#!/usr/bin/env python
# coding:utf-8

from datetime import date,datetime,timedelta

#计算两个日期的相差天数
#使用date
def day_diff(date1, date2):
    day2 = date(*date2)
    day1 = date(*date1)
    day = day2-day1
    return abs(day.days)

#使用datetime
def day_diff1(date1, date2):
    d1 = datetime(*date1)
    d2 = datetime(*date2)
    return int(abs(d1-d2).total_seconds()/3600/24)

if __name__ == '__main__':
    day1 = (2014, 8, 27)
    day2 = (2014, 1, 1)
    print(day_diff(day1, day2))
    print(day_diff1(day1, day2))
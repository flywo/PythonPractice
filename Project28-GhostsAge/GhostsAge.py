#!/usr/bin/env python
# coding:utf-8


def check(o):
    a, b = 1,1
    age = 0
    while o != 10000:
        age += 1
        if age == b:
            o += b
            a,b = b, a+b
        else:
            o -= 1
    return age

if __name__ == '__main__':
    print(check(10000))
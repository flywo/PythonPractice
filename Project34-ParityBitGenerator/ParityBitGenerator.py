#!/usr/bin/env python
# coding:utf-8


def check1(message):
    return ''.join(chr(a>>1) for a in message if bin(a).count('1')%2==0)

def check2(message):
    def check(c):
        return bin(c).count('1') & 1 == 0
    return ''.join(chr(c>>1) for c in message if check(c))

if __name__ == '__main__':
    arr = [135, 134, 124, 233,
                    209, 81, 42, 202,
                    198, 194, 229, 215,
                    230, 146, 28, 210,
                    145, 137, 222, 158,
                    49, 81, 214, 157]
    print(check1(arr))
    print(check2(arr))
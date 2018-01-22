#!/usr/bin/env python
# coding:utf-8

import itertools

def check(k, n):
    two_sides = ''.join(2*list(str(a) for a in range(n)))
    k = min(k, n)
    return ','.join(two_sides[i:i+k] for i in range(0, 2*n, k))

def check1(k, n):
    import string
    sides = string.digits[:n]*2
    step = min(k, n)
    return ','.join([[sides[i:i+step]] for i in range(0,len(sides),step)])

if __name__ == '__main__':
    print(check(2, 5))
    print(check(2, 5))

    func = lambda k,n:','.join(('0123456789'[:n]*2)[i:i+min(n,k)] for i in range(0,2*n,min(n,k)))
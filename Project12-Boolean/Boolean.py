#!/usr/bin/env python
# coding:utf-8

def boolean(x,y,operation):
    if operation == "conjunction" or operation == u"conjunction":
        if x == 0 or y == 0:
            return 0
        else:
            return 1
    elif operation == "disjunction" or operation == u"disjunction":
        if x == 1 or y == 1:
            return 1
        else:
            return 0
    elif operation == "implication" or operation == u"implication":
        if x == y or (x == 0 and y == 1):
            return 1
        else:
            return 0
    elif operation == "exclusive" or operation == u"exclusive":
        if x == y:
            return 0
        else:
            return 1
    elif operation == "equivalence" or operation == u"equivalence":
        if x == y:
            return 1
        else:
            return 0
    else:
        return None


#大神方案
def check1(x,y,operation):
    if operation == 'con': return x & y
    if operation == 'dis': return x | y
    if operation == 'imp': return (1 ^ x) | y
    if operation == 'exc': return x ^ y
    if operation == 'equ': return x ^ y - 1


if __name__ == '__main__':
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"


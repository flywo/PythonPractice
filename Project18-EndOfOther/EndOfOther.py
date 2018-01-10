#!/usr/bin/env python
# coding:utf-8


def check(words_set):
    if len(words_set) == 1:
        return False
    words = sorted(words_set, key=len)
    for con in words:
        if words.index(con) == len(words)-1:
            break
        for x in words[words.index(con)+1:]:
            if con == x[len(x)-len(con):]:
                return True
    return False


#大神，直接使用endswith来判断
def check1(words):
    for w1 in words:
        for w2 in words:
            if w1 != w2 and (w1.endswith(w2) or w2.endswith(w1)):
                return True
    return False


def check2(words):
    words = sorted(list(words), key=len)
    while words:
        w = words.pop()
        if w.endswith(tuple(words)):
            return True
    return False

def check3(words):
    l = sorted(words, key=lambda x: x[::-1])
    for i in range(1, len(l)):
        if l[i].endswith(l[i-1]):
            return True
    return False

from itertools import starmap as s, permutations as p

if __name__ == '__main__':
    se = {"hello", "la", "hellow"}
    print(check(se))
    print(check1(se))
    print(check2(se))
    #排列组合p
    print(list(p(se, 2)))
    fun = lambda w: any(s(str.endswith, p(w, 2)))
    print(fun(se))
    print(check3(se))
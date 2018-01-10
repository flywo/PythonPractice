#!/usr/bin/env python
# coding:utf-8

def non_repeat(line):
    if len(set(line)) == 1:
        return line[0]
    if len(line) == 0:
        return ''
    line = line[::-1]
    result = {}
    for w in range(2,len(line)+1):
        for s in range(0,len(line)+1-w):
            sub = line[s:s+w]
            if len(set(sub)) == len(sub):
                result[w] = sub
    return result[max(result.keys())][::-1]


def check1(line):
    return (line if len(line)==len(set(line)) else
            max(non_repeat(line[:-1]),non_repeat(line[1:]),key=len))


def intervals(line):
    last = {}
    start = end = 0
    for i,letter in enumerate(line):
        end += 1
        if letter in last and start <= last[letter]:
            start = last[letter] + 1
        yield line[start:end]
        last[letter] = i
def check2(line):
    return max(intervals(line), key=len, default='')


if __name__ == '__main__':
    str = 'abdjwawk'
    print(non_repeat(str))
    print(check1(str))
    print(check2(str))

    fun = lambda s,r=range(99):max([s[i:j] for i in r for j in r],
                                   key=lambda x:len(x)*bool(len(x)==len(set(x))))
    print(fun(str,range(len(str))))
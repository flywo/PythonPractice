#!/usr/bin/env python
# coding:utf-8

import re
from string import punctuation

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
PUNCTUATION = ',.!?'

#找出元音辅音交替的单次
#自写版本
def check(text):

    def checkStr(text):
        if len(text) <= 1:
            return False
        for x in range(1, len(text)):
            f = 0
            s = 0
            if text[x-1].upper() in VOWELS:
                f = -1
            elif text[x-1].upper() in CONSONANTS:
                f = 1
            else:
                return False
            if text[x].upper() in VOWELS:
                s = -1
            elif text[x].upper() in CONSONANTS:
                s = 1
            else:
                return False
            if f+s != 0:
                return False
        return True

    content = re.split('[,. ?]',text)
    result = 0
    for str in content:
        if checkStr(str):
            result += 1
    return result

#大神解决方案，替换掉元音和辅音
def check1(text):
    text = text.upper()
    for c in PUNCTUATION:
        text = text.replace(c, ' ')
    for c in VOWELS:
        text = text.replace(c, 'v')
    for c in CONSONANTS:
        text = text.replace(c, 'c')
    words = text.split(' ')
    count = 0
    for word in words:
        if len(word)>1 and word.isalpha():
            if word.find('vv') == -1 and word.find('cc') == -1:
                count += 1
    return count

#比较相邻字符
def check2(text):
    for p in punctuation:
        text = text.replace(p, ' ')
    cnt = 0
    for token in text.split(' '):
        if len(token) < 2: continue
        token = token.upper()
        outer = set(token[::2])
        inner = set(token[1::2])
        if (outer.issubset(VOWELS) and inner.issubset(CONSONANTS)) or \
                (inner.issubset(VOWELS) and outer.issubset(CONSONANTS)):
            cnt += 1
    return cnt

#使用yield生成器
    #判断是否是不合规的
def striped(word):
    for forbidden in 'd','v'*2, 'c'*2:
        if forbidden in word:
            return False
    return len(word)>1
    #将text替换掉
def encode(text):
    for char in text:
        if char.lower() in 'aeiouy':
            yield 'v'
        elif char.isalpha():
            yield 'c'
        elif char.isdigit():
            yield 'd'
        else:
            yield 'p'
def check3(text):
    encoded = ''.join(encode(text))
    words = encoded.split('p')
    return sum(map(striped, words))

#简短的代码
def check4(text):
    text = ''.join('V' if t in 'AEIOUY' else
                   'C' if t.isalpha() else
                   'D' if t.isdigit() else
                   ' '
                   for t in text.upper())
    return sum('VV' not in token and
               'CC' not in token and
               'D' not in token and
               len(token)>1
               for token in text.split())

if __name__ == '__main__':
    str = 'Dog,cat,mouse,bird.Human.'
    print(check(str))
    print(check1(str))
    print(check2(str))
    print(check3(str))
    print(check4(str))
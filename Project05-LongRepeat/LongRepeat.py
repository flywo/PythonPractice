#!/usr/bin/env python
# coding:utf-8

from itertools import groupby

#找出一个字符串中，相同字母连续出现的最多的字符串，返回他的长度
'''
依次遍历字符串，找出相同的字母的串
'''
def check(text):
    if len(text)==0: return 0
    x = 1
    result = {} #存放结果
    count = 1 #字母出现次数
    begin = 0 #切片起始位置
    while(x < len(text)):
        if text[x-1] != text[x]:
            result[text[begin:begin+count]] = count
            begin = begin + count
            count = 1
        elif x+1 == len(text):
            count += 1
            result[text[begin:begin + count]] = count
        else:
            count += 1
        x += 1
    return max(result.items(), key=lambda item: item[1])[1]

'''
通过另一种方式遍历获得
'''
def check1(text):
    temp = ['',0,0] # 上一个字母 当前累计字母个数 最大字母个数
    for str in text:
        if str==temp[0]:
            temp[1]+=1
        else:
            temp[0]=str
            temp[1]=1
        if temp[1]>temp[2]:
            temp[2]=temp[1]
    return temp[2]

if __name__ == '__main__':
    str = 'aaabbbcccddddaaaaaa'
    print(check(str))
    print(check1(str))

    for k,v in groupby(str):
        print(k)
        print(list(v))
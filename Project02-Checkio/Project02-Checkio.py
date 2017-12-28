#!/usr/bin/env python
# coding:utf-8

import string

'''
checkio作用是检查输入的text，检查其中包含的小写字母的个数，输出包含最多的值，大写字母按照小写字母处理
'''

def checkio(text):
    text = text.lower()
    return min([-1*text.count(ch), ch] for ch in string.ascii_lowercase)[1]

'''
checkStr作用是检查输入的text，检查出包含的小写字母的个数，并按照排序输出，大写字母按照小写字母处理
'''
def checkStr(text):
    text = text.lower()
    return sorted([[text.count(ch), ch] for ch in string.ascii_lowercase if text.count(ch) != 0], reverse = True)

'''
checkNum检查输入的数组，剔除掉唯一的元素，留下有重复的元素
'''
def checkNum(data):
    return [x for x in data if data.count(x) > 1]

'''
checkPWD检查字符串，长度与是否包含数字大小写字母
'''
def checkPWD(pwd):
    if len(pwd)<10:
        return False
    return any(ch.isdigit() for ch in pwd) and any(ch.islower() for ch in pwd) and any(ch.isupper() for ch in pwd)

if __name__ == '__main__':
    text = 'abskfsakjfslakjlfhdalfkj'
    result = checkio(text)
    print('最后最多的字母是:'+result)

    result = checkStr(text)
    print(result)

    arr = [1,2,3,4,5,3,3,2]
    print(checkNum(arr))

    print(checkPWD('abcaaaAaaaaaa'))
#!/usr/bin/env python
# coding:utf-8

import string

'''
要求：计算出一个字符串中，字母出现最初的字母，如果出现的字母次数相同，则只获取按照字母表排序最小的字母
'''

'''
max:本函数是迭代对象iterable进行比较，找出最大值返回。当key参数不为空时，就以key的函数对象为判断的标准。如果有多个相同，只返回第一个。
'''
def check1(text):
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)

'''
要求：找出一段字符串中，包含的指定字符的个数
'''
def check2(text,words):
    count = 0
    text = text.lower()
    for word in words:
        if word in text:
            count+=1
    return count
def check2_1(text,words):
    count = 0
    text = text.lower()
    for word in words:
        if text.count(word):
            count+=1
    return count
def check2_2(text,words):
    return sum(map(text.lower().__contains__, words))
def check2_3(text,words):
    return sum(w in text.lower() for w in words)


'''
检查是否是三个字符相连
'''
def check3(game_result):
    for ch in game_result:
        result = checkResult(ch)
        if result != 'D': return result
    x = 0
    while x < 3:
        chs = [game_result[0][x], game_result[1][x], game_result[2][x]]
        result = checkResult(chs)
        if result != 'D':return result
        x += 1
    result = checkResult([game_result[0][0], game_result[1][1], game_result[2][2]])
    if result != 'D': return result
    result = checkResult([game_result[0][2], game_result[1][1], game_result[2][0]])
    return result
def checkResult(mutable):
    if 'X' not in mutable and '.' not in mutable: return 'O'
    if 'O' not in mutable and '.' not in mutable: return 'X'
    return 'D'
def check3_1(gr):
    w = 'D'
    for i in gr:
        if i[0]==i[1]==i[2]!='.':
            w = i[0]
    for i in range(3):
        if gr[0][i]==gr[1][i]==gr[2][i]!='.':
            w = gr[0][i]
    if gr[0][0]==gr[1][1]==gr[2][2]!='.':
        w = gr[0][0]
    if gr[2][0]==gr[1][1]==gr[0][2]!='.':
        w = gr[2][0]
    return w
def check3_2(gr):
    rows = gr
    #zip:接受任意多个序列，返回一个tuple列表
    cols = map(''.join, zip(*rows))
    #map:对参数序列中每一个元素调用function函数，返回包含结果的新列表
    diags = map(''.join, zip(*[(r[i], r[2-i]) for i, r in enumerate(rows)]))
    lines = rows + list(cols) + list(diags)
    return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'
def check3_3(gr):
    for i in range(3):
        if gr[i][0] in ['O','X'] and gr[i][0]==gr[i][1]==gr[i][2]:
            return gr[i][0]
        if gr[0][i] in ['O','X'] and gr[0][i]==gr[1][i]==gr[2][i]:
            return gr[0][i]
    if gr[1][1] in ['O','X'] and (gr[0][0]==gr[1][1]==gr[2][2] or gr[2][0]==gr[1][1]==gr[0][2]):
        return gr[1][1]
    return 'D'


'''
检查国际象棋中，那几个兵是安全的
'''
def check4(pawns):
    pawn_index = set()
    for pawn in pawns:
        row = int(pawn[1])-1
        col = ord(pawn[0])-97
        pawn_index.add((col,row))
    count = 0
    for index in pawn_index:
        if (index[0]-1,index[1]-1) in pawn_index or (index[0]+1,index[1]-1) in pawn_index:
            count += 1
    return count


if __name__ == '__main__':
    text = "How aresjfhdskfhskd you?"
    words = {"how", "are", "you", "hello"}
    array = [".O.","XXX",".O."]
    pawns = {"b4", "c4", "d4", "e4", "f4", "g4", "e5"}

    print(check1(text))#c

    print(check2(text,words))
    print(check2_1(text,words))
    print(check2_2(text,words))
    print(check2_3(text,words))

    print(check3(array))
    print(check3_1(array))
    print(check3_2(array))
    print(check3_3(array))

    print(check4(pawns))
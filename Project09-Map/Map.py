#!/usr/bin/env python
# coding:utf-8

#自己写的方法
def turn(arr, right):
    line1 = [0, 1, 2, 3]
    line2 = [3, 2, 1, 0]

    first = []
    second = []
    third = []
    forth = []
    for str in arr:
        content = []
        for str in str:
            content.append(str)
        first.append(content)
        second.append(content[:])
        third.append(content[:])
        forth.append(content[:])

    x = 0
    for r in line2:
        y = 0
        for l in line1:
            forth[l][r] = first[x][y]
            y += 1
        x += 1

    x = 0
    for l in line2:
        y = 0
        for r in line2:
            third[l][r] = first[x][y]
            y += 1
        x += 1

    x = 0
    for l in line1:
        y = 0
        for r in line2:
            second[r][l] = first[x][y]
            y += 1
        x += 1
    if right:
        return (first, forth, third, second)
    return (first, second, third, forth)

def check(cipher_grille, ciphered_password):

    r = turn(ciphered_password, False)
    c = turn(cipher_grille, True)
    arr = []
    for item1 in c:
        x = 0
        for item2 in item1:
            y = 0
            for item3 in item2:
                if item3 == 'X':
                    arr.append([x, y])
                y += 1
            x += 1

    x = 0
    res = ''
    for item1 in [r[0],r[0],r[0],r[0]]:
        y = 0
        while (y < 4):
            item = arr[x]
            res += item1[item[0]][item[1]]
            y += 1
            x += 1
    return res


#大神解决方案：使用zip
def check1(grill, cypher):
    password = ''
    for _ in grill:
        for grill_row, cypher_row in zip(grill, cypher):
            for grill_letter, cypher_letter in zip(grill_row, cypher_row):
                if grill_letter == 'X':
                    password += cypher_letter
        row1, row2, row3, row4 = grill
        grill = tuple(zip(row4, row3, row2, row1))
    return password

#将数组翻转后比较
def check2(grill, cypher):
    def rot(g):
        return [[g[3-x][y] for x in range(4)] for y in range(4)]
    password = []
    for i in range(4):
        password += [cypher[y][x] for y in range(4) for x in range(4) if grill[y][x] == 'X']
        grill = rot(grill)
    return ''.join(password)

#使用zip和map
def check3(grill, cypher):
    pwd, j = '', ''.join
    for _ in range(4):
        pwd += j(c for g,c in zip(j(grill), j(cypher)) if g == 'X')
        grill = list(map(j, list(zip(*grill[::-1]))))
    return pwd

if __name__ == '__main__':
    content = (('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi'))
    print(check(*content))
    print(check1(*content))
    print(check2(*content))
    print(check3(*content))
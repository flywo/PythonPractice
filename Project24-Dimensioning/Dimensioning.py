#!/usr/bin/env python
# coding:utf-8

def check(ring, *flows):
    ring += ring
    res = []
    for x,y in flows:
        z = sorted(x)
        x = z[0]+z[1]
        x1 = ring.index(x[0])
        x2 = ring.index(x[1])
        str1 = ring[x1:x2+1]
        x3 = ring.index(x[1])
        x4 = ring.index(x[0],x1+1)
        str2 = ring[x3:x4+1]
        res.append(min((str1,str2),key=len))
    result = {}
    for x in res:
        for item in [frozenset(x[y-1:y+1]) for y in range(1,len(x))]:
            if item in result.keys():
                result[item] += flows[res.index(x)][1]
            else:
                result[item] = flows[res.index(x)][1]
    arr = sorted(result.values(), reverse=True)
    ress = [0,0,0,0,0]
    for x in arr:
        if 40<x<=100:
            ress[0] += 1
        elif 10<x<=40:
            ress[1] += 1
        elif 1<x<=10:
            ress[2] += 1
        elif 0.1<x<=1:
            ress[3] += 1
        else:
            ress[4] += 1
    return ress


if __name__ == '__main__':
    res = ("ABCDEFGH", ("AD", 4), ("EA", 41))

    print(check(*res))

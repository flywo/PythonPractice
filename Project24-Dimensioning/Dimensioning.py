#!/usr/bin/env python
# coding:utf-8

def check(ring, *flows):
    ring *= 2
    res = []

    #获取最近的路
    for x,y in flows:
        sub = x[0]+max(ring.split(x[0]))+x[0]
        sub = sub.split(x[1])
        if len(sub[0])==len(sub[1]):
            sub = sub[0] if sub[0][0] == x[0] else sub[1]
        else:
            sub = min(sub, key=len)
        res.append(str(sub+x[1]) if sub[0]==x[0] else str(x[1]+sub))

    #获得两点之间的流量
    result = {}
    for i,x in enumerate(res):
        for item in [frozenset(x[y-1:y+1]) for y in range(1,len(x))]:
            if item in result.keys():
                result[item] += flows[i][1]
            else:
                result[item] = flows[i][1]

    #计算出需要的带宽
    arr = sorted(result.values(), reverse=True)
    ress = [0,0,0,0,0]
    for x in arr:
        if x > 100:
            if x%100 == 0:
                ress[0] += x//100
            else:
                ress[0] += x//100+1
        elif 40<x<=100:
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
    res = (["ABCDEFGH",["AE",170],["EA",10000],["HF",1]])

    print(check(*res))

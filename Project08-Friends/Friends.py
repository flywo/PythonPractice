#!/usr/bin/env python
# coding:utf-8


#计算出是否是有关联的
#把节点都作为key，有关系的节点作为value
def check(network, first, second):
    dic = {}
    for content in network:
        node = content.split('-')
        if node[0] in dic.keys():
            dic[node[0]].add(node[1])
        else:
            dic[node[0]] = set([node[1]])
        if node[1] in dic.keys():
            dic[node[1]].add(node[0])
        else:
            dic[node[1]] = set([node[0]])


    for k1,v1 in dic.items():
        for k2,v2 in dic.items():
            if k1!=k2:
                for value in v2:
                    if k1 in v2 or value in v1:
                        for v in v2:
                            v1.add(v)
    return second in dic[first]

#将所有有关系的node放到一个set中，然后判断给出的node是否在同一个set中即可
def check1(network, first, second):
    setlist = []
    for content in network:
        s = set(content.split('-'))
        for t in setlist[:]:
            if t & s:
                s |= t
                setlist.remove(t)
        setlist.append(s)
    return any(set([first, second]) <= s for s in setlist)

#通过指定的Note去查找，而不是先分组
def check2(network, first, second):
    team = {first}
    for _ in network:
        for edge in network:
            pair = set(edge.split('-'))
            if pair & team:
                team |= pair
    return second in team

#简短的写法
def check3(netwrok, first, second):
    graph, edges = {first}, [set(e.split('-')) for e in netwrok]
    for _ in edges:
        graph.update(*filter(graph.intersection, edges))
    return second in graph

if __name__ == '__main__':
    arr = (
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout")
    print(check(*arr))
    print(check1(*arr))
    print(check2(*arr))
    print(check3(*arr))
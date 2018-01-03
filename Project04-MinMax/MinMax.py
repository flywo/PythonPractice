#!/usr/bin/env python
# coding:utf-8


#自定义实现max和min


def get_from_sorted(args, key, reverse):
    if len(args) == 1:
        args = iter(args[0])
    return sorted(args, key=key, reverse=reverse)[0]
'''
采用先排序，再输出结果的方式
'''
def min(*args, key=None):
    return get_from_sorted(args, key, False)

def max(*args, key=None):
    return get_from_sorted(args, key, True)

'''
采用遍历的方式查找
'''
def min1(*args, **kwargs):
    key = kwargs.get('key', None)
    if key == None:
        key = lambda x :x
    if len(args) == 1:
        args = iter(args[0])
        m = next(args)
    else:
        m = args[0]
    for v in args:
        if key(v) < key(m):
            m = v
    return m
def max1(*args, **kwargs):
    key = kwargs.get('key', None)
    if key == None:
        key = lambda x :x
    if len(args) == 1:
        args = iter(args[0])
        m = next(args)
    else:
        m = args[0]
    for v in args:
        if key[v] > key(m):
            m = v
    return m


if __name__ == '__main__':
    arr = [1,4,3,2,0]

    print('最大：%d,最小：%d' % (max(arr), min(arr)))

    # print('max:%d,min:%d' % (max1(arr), min1(arr)))

    
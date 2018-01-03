#!/usr/bin/env python
# coding:utf-8

#计算出一个序列的中位数，即偶数个时，中间两数相加/2，奇数时，中间数
#先排序，然后计算出
def check(data):
    data.sort()
    count = len(data)
    if count%2 == 0:
        return (data[int(count/2)-1]+data[int(count/2)])/2
    else:
        return data[int(count/2)]

#利用反向计算
def check1(data):
    data.sort()
    half = (len(data)-1)//2 #地板除，只取整数部分
    return (data[half] + data[len(data)-1-half])/2


if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7]
    print(check(arr))
    print(check1(arr))
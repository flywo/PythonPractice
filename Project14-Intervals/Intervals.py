#!/usr/bin/env python
# coding:utf-8


def create_intervals(data):
    arr = sorted(list(data))
    result = []
    interval = set()
    if len(arr) == 1:
        result.append([arr[0]])
    for x in range(1, len(arr)):
        if arr[x]-arr[x-1] == 1:
            interval.add(arr[x])
            interval.add(arr[x-1])
        else:
            if x == 1:
                result.append({arr[x-1]})
                interval.add(arr[x])
                continue
            result.append(interval.copy())
            interval.clear()
            interval.add(arr[x])
        if x == len(arr)-1:
            result.append(interval)
    return [(min(content), max(content)) for content in result]


#大神方案
def check1(data):
    left = [x for x in data if x-1 not in data]
    right = [x for x in data if x+1 not in data]
    return list(zip(sorted(left), sorted(right)))

def check2(data):
    if len(data) < 1:
        return []
    data = sorted(data)
    intervals = []
    current_intervals = [data[0], data[0]]
    for number in data[1:]:
        if number-current_intervals[1] == 1:
            current_intervals[1] = number
        else:
            intervals.append((current_intervals[0], current_intervals[1]))
            current_intervals = [number, number]
    intervals.append((current_intervals[0], current_intervals[1]))
    return intervals

def check3(data):
    res = sorted(x for x in data for i in [-1, 1] if x+i not in data)
    return [(x,y) for x,y in zip(res[::2], res[1::2])]

if __name__ == '__main__':
    da = {1, 2, 3, 4, 5, 7, 8, 12}
    print(create_intervals(da))
    print(check1(da))
    print(check2(da))
    print(check3(da))

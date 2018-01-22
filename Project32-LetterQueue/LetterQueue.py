#!/usr/bin/env python
# coding:utf-8

def check1(commands):
    queue = []
    for i in commands:
        temp = i.split()
        if temp[0].strip() == 'PUSH':
            queue.append(temp[1].strip())
        elif temp[0].strip() == 'POP':
            queue = queue[1:]
    return ''.join(queue)


def check2(commands):
    import collections
    queue = collections.deque()
    for com in commands:
        if com.startswith('PUSH'):
            queue.append(com[-1])
        elif queue:
            queue.popleft()
    return ''.join(queue)


def check3(commands):
    s = ''
    for cmd in commands:
        if 'PUSH' in cmd:
            s += cmd.split(' ')[1]
        else:
            s = s[1:] if s else ''
    return s


if __name__ == '__main__':
    arr = ["PUSH A", "POP", "POP", "PUSH Z",
                         "PUSH D", "PUSH O", "POP", "PUSH T"]
    print(check1(arr))
    print(check2(arr))
    print(check3(arr))
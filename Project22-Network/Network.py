#!/usr/bin/env python
# coding:utf-8

import itertools

def check(data):
    ips = list(zip(*[map(int, x.split('.')) for x in data]))
    result = [max([y^z for y,z in itertools.combinations(x, 2)]) for x in ips]
    ip_len = 0
    ip = []
    for i,x in enumerate(result):
        if x == 0:
            ip_len += 8
            ip.append(str(ips[i][0]))
        else:
            ip_len += (10-len(bin(x)))
            ip.append(str((ips[i][0]>>(len(bin(x))-2))<<(len(bin(x))-2)))
            break
    for _ in range(len(ip), 4):
        ip.append('0')
    return '.'.join(ip)+'/{}'.format(ip_len)


def check1(data):
    from ipaddress import IPv4Address, IPv4Network
    ipmin, *_, ipmax = sorted(map(IPv4Address, data))
    spread = (int(ipmin) ^ int(ipmax)).bit_length()
    return str(IPv4Network(ipmin).supernet(prefixlen_diff=spread))


if __name__ == '__main__':
    arr = ["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]
    print(check(arr))
    print(check1(arr))
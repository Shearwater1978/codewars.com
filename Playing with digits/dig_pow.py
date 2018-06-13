#!/usr/bin/env python
# -*- coding: utf-8 -*-


def dig_pow(n, p):
    sum_out = 0
    for item in str(n):
        sum_out += int(item) ** p
        p += 1
    if sum_out % int(n) == 0:
        return sum_out // int(n)
    return -1


print(dig_pow(89, 1))
print(dig_pow(92, 1))
print(dig_pow(46288, 3))

#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_sum(a,b):
    summ = 0
    if a == b:
        return a
    else:
        if a < b:
            for item in range(a, b+1):
                summ += item
        else:
            for item in range(b, a + 1):
                summ += item
        return summ


print(get_sum(1, 0))
print(get_sum(1, 2))
print(get_sum(0, 1))
print(get_sum(1, 1))
print(get_sum(-1, 0))
print(get_sum(-1, 2))

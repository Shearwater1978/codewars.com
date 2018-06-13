#!/usr/bin/env python
# -*- coding: utf-8 -*-


def digital_root(n):
    if len(str(n)) == 1:
        return n
    else:
        summ = 0
        for item in str(n):
            summ += int(item)
        digital_root(summ)


print(digital_root(132189))

#!/usr/bin/env python
# -*- coding: utf-8 -*-


def digital_root(n):
    if len(str(n)) > 1:
        summ = 0
        for item in str(n):
            summ += int(item)
        return digital_root(summ)
    elif len(str(n)) == 1:
        return(n)


print(digital_root(132189))

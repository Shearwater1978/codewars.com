#!/usr/bin/env python
# -*- coding: utf-8 -*-


def filter_list(l):
    out = []
    for item in l:
        if type(item) == int:
            out.append(item)
    return(out)


filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

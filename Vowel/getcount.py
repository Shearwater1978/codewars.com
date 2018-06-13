#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re


def getCount(inputStr):
    import re
    pattern = r"a|e|i|o|u"
    num_vowels = 0
    return len(re.findall(pattern, inputStr))


getCount("abracadabra")


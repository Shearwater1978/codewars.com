#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re


def validate_pin(pin):
    pattern = r"\b([0-9]{4}|[0-9]{6})\b"
    if re.match(pattern, pin):
        return(True)
    else:
        return(False)


validate_pin("1")
validate_pin("-1.234")
validate_pin(".234")
validate_pin("1234")
validate_pin("098765")

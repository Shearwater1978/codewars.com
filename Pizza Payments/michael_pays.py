#!/usr/bin/env python
# -*- coding: utf-8 -*-


def michael_pays(costs):
    if costs < 5:
        pay = costs
    elif costs // 3 < 10:
        pay = costs - round(costs / 3, 3)
    else:
        pay = costs - 10
    if (pay % 10 != 0.0):
        pay = round(pay, 2)
    else:
        pay = round(pay)
    return pay


michael_pays(15)
michael_pays(4)
michael_pays(30)
michael_pays(80)
michael_pays(22)
michael_pays(5.9181)
michael_pays(28.789)
michael_pays(4.325)

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   : 2021/1/11 14:24
# @Author : Snowball

test = [1, 1, 2, 3, 5, 8, 13, 21]


def fib_dp(n):
    a, b = 1, 1
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    return c


print(fib_dp(3))
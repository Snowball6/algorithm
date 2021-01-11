#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   : 2021/1/11 15:15
# @Author : Snowball

# 假如有m个不同面值的硬币，它们的面值分别为 1=v1 < v2 < v3,.. <vm。 现在希望把价值为V的纸钞换成硬币，但要求是使用越少量的硬币来换取，如何做？
import sys


def minCoins(coins, V, C):

    table = [0 for i in range(C + 1)]

    # Base case
    table[0] = 0

    # 初始化
    for i in range(1, V + 1):
        table[i] = sys.maxsize

    for i in range(1, C + 1):

        # Go through all coins smaller than i
        for j in range(V):
            if (coins[j] <= i):
                sub_res = table[i - coins[j]]
                if (sub_res != sys.maxsize and
                        sub_res + 1 < table[i]):
                    table[i] = sub_res + 1
    return table[C]


arr = [1, 2, 3]
m = len(arr)
n = 100
print(minCoins(arr, m, n))
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   : 2021/1/11 14:38
# @Author : Snowball


# 给定数组 a1, a2,... am, 找出一个子序列使得它的相加之和最大


def max_subseq_sum(arr):
    max_current = 0
    for i in range(0, len(arr)):
        if max_current + arr[i] >= arr[i]:
            max_current += arr[i]
        else:
            max_current = arr[i]
    return max_current


print(max_subseq_sum([-2, -3, 4, -1, -2, 1, 5, -3]))

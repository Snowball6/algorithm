#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   : 2021/1/12 9:42
# @Author : Snowball


# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

# dp(n) = dp(n-1) + dp(n-2)
def dance_steps(n):
    if n <= 1:
        return 1
    dp = [0 for i in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp)
    return dp[n] % 1000000007

print(dance_steps(0))

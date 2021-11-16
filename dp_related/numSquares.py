# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: numSquares.py
@time: 2021/9/6 17:37
@desc: 完全平方数， 组成n的完全平方数的个数最少
'''


def numSquares(n: int) -> int:
    dp = [0] + [float('inf')]*n
    for i in range(1,n + 1):
        j = i * i
        for ii in range(j, n + 1):
            dp[ii] = min(dp[ii], dp[ii - j] + 1)
    return dp[n]

n = 12
print(numSquares(12))
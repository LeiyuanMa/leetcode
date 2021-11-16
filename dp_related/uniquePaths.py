# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: uniquePaths.py
@time: 2021/9/9 22:29
@desc: 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）
'''

def uniquePaths(m,n):
    dp = [[1]*n] + [[1]+[0]*(n-1) for _ in range(m-1)]
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j]+dp[i][j-1]
    return dp[m-1][n-1]


m = 3
n = 7
print(uniquePaths(m,n))
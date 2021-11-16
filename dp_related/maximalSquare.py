# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: maximalSquare.py
@time: 2021/9/2 16:24
@desc: 
'''


def maximalSquare(matrix) -> int:
    m = len(matrix)
    n = len(matrix[0])
    maxSide = 0
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1' and (i == 0 or j == 0):
                dp[i][j] = 1
            elif matrix[i][j] == '0':
                dp[i][j] = 0
            elif matrix[i][j] == '1':
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
            maxSide = max(maxSide, dp[i][j])
    return maxSide


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

print(maximalSquare(matrix))
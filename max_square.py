# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: max_square.py
@time: 2021/11/9 11:24
@desc: 
'''

matrix = [[1, 0, 1, 0, 0,],
           [1, 0, 0, 1, 1],
           [1, 1, 1, 1, 1],
           [1 ,0 ,1, 1 ,1]]


def max_square(matrix):
    max_area = 0
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0] *n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if (i==0 or j==0) and matrix[i][j] == 1:
                dp[i][j] = 1
            elif matrix[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
            max_area = max(max_area, dp[i][j]*dp[i][j])
    return max_area


print(max_square(matrix))


# #####
# 1：坐对：1/n   不对：1-1/n
#
# 2:坐对：1/n + (1-1/n)*(n-2)/(n-1) P(n2/n1)
# ---->:P(坐对)+p(没有坐到当前人所属的位置|上一个人没坐对)
#
# 3:坐对：1/n + (1-1/n)*(n-3)/(n-2) + (1-P(n2/n1))*(n-3)/(n-2) p(n3/n2)



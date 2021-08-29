# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: minPathSum.py
@time: 2021/8/27 18:45
@desc: 
'''


def minPathSum(grid) -> int:
    sum = 0

    def backtrace(i, j, current_sum):
        if (i, j) == (m - 1, n - 1):
            sum = min(current_sum, sum)
            return

        for ii in range(i, n):
            for jj in range(j, m):
                current_sum += grid[ii][jj]
                backtrace(ii+1, jj+1, current_sum)
                current_sum -= grid[ii][jj]
    m = len(grid)
    if m == 0:
        return 0
    n = len(grid[0])
    backtrace(0, 0, 0)
    return sum

grid = [[1,3,1],[1,5,1],[4,2,1]]
minPathSum(grid)
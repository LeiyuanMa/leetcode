# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: rotate.py
@time: 2021/8/27 18:26
@desc: 
'''


def rotate(matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    matrix_new = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix_new[j][n - i - 1] = matrix[i][j]
    matrix[:] = matrix_new
matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
print(matrix)
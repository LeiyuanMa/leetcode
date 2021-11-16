# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: countBits.py
@time: 2021/9/7 14:52
@desc: Brian Kernighan 算法的原理是：对于任意整数 xx，令 x=x~\&~(x-1)x=x & (x−1)，该运算将 xx 的二进制表示的最后一个 11 变成 00。
        给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数
'''

def countBits(num):
    ones = 0
    while num:
        num = num&(num-1)
        ones+=1
    return ones

num = 10
print(countBits(num))
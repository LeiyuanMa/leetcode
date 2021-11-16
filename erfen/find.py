# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: find.py
@time: 2021/8/7 23:09
@desc: 求数组中比左边元素都大同时比右边元素都小的元素，返回这些元素的索引
'''

def find(nums):
    n = len(nums)
    res = []
    left_max = [float("-inf") for i in range(n)] # [0, i) 最大的值
    right_min = [float("inf") for i in range(n)] # (i, n) 最小的值
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], nums[i-1])
    print(left_max)
    for i in range(n-2,-1,-1):
        print(i)
        right_min[i] = min(right_min[i+1], nums[i+1])
    print(right_min)
    for i in range(n):
        if left_max[i] < nums[i] < right_min[i]:
            res.append(i)
    return res
print(find([2,3,1,8,9,20,12]))
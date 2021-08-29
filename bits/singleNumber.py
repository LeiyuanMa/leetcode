# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: singleNumber.py
@time: 2021/8/29 19:18
@desc: 
'''


def singleNumber(nums) -> int:
    res = nums[0]
    for i in range(1, len(nums)):
        res ^= nums[i]
    return res

print(singleNumber([2,2,1]))
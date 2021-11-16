# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: moveZeroes.py
@time: 2021/9/6 18:17
@desc: 
'''

def moveZeroes(nums):
    n = len(nums)
    left = right = 0
    while right < n:
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1

moveZeroes([0,1,0,3,12])

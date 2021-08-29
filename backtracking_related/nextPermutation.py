# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: nextPermutation.py
@time: 2021/8/27 15:00
@desc: 
'''


def nextPermutation(nums):
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = len(nums) - 1
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    left, right = i + 1, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums



nums = [1,2,3]
print(nextPermutation(nums))
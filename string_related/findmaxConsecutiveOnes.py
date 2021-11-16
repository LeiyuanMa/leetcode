# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: findmaxConsecutiveOnes.py
@time: 2021/11/1 16:16
@desc: 通过翻转k个0，求字符串中连续1的长度,字节1面
'''


def findMax(nums, k):
    left, right = 0, 0
    zeros = 0
    res = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
        while (zeros > k):
            if nums[left] == 0:
                zeros -= 1
            left += 1
        res = max(res, right - left + 1)
    return res


nums = [1, 0, 1, 1, 0]
k = 1
print(findMax(nums, k))

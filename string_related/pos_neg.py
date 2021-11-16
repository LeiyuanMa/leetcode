# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: pos_neg.py
@time: 2021/10/27 23:18
@desc: 
'''


def pos_neg(nums):
    size = len(nums)
    pos_num = sum(n > 0 for n in nums)
    neg_num = sum(n < 0 for n in nums)
    p, n = 0, 0
    if pos_num >= neg_num:
        n = 1
    else:
        p = 1
    while p < size and n < size:
        while p < size and nums[p] > 0:
            p += 2
        while n < size and nums[n] < 0:
            n += 2
        if p >= size or n >= size:
            break

        nums[p], nums[n] = nums[n], nums[p]
    return nums


nums = [1, -1, -2, -3, -4, -5, 2, 3, 4, 5]
print(pos_neg(nums))

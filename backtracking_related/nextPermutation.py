# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: nextPermutation.py
@time: 2021/8/27 15:00
@desc: 我们需要将一个左边的「较小数」与一个右边的「较大数」交换，以能够让当前排列变大，从而得到下一个排列。

    同时我们要让这个「较小数」尽量靠右，而「较大数」尽可能小。当交换完成后，「较大数」右边的数需要按照升序重新排列。
    这样可以在保证新排列大于原来排列的情况下，使变大的幅度尽可能小。
'''


def nextPermutation(nums):
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    print(i)
    # 当前已经是最大的排列了，直接返回逆序后的值
    if i >= 0:
        j = len(nums) - 1
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        print(j)
        nums[i], nums[j] = nums[j], nums[i]

    # 当交换完成后，「较大数」右边的数需要按照升序重新排列。
    left, right = i + 1, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums



nums = [5,4,7,5,3,2]
print(nextPermutation(nums))
# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: equal_diff.py
@time: 2021/11/3 20:40
@desc: 蚂蚁金服1面
'''


def equal_diff(nums):
    size = len(nums)
    if size < 3:
        return 0
    dp = [0] * size

    for i in range(2, size):
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            dp[i] = dp[i - 1] + 1
    return sum(dp)


nums = [1, 2, 3, 4]
print(equal_diff(nums))

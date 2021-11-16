# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: findTargetSumWays.py
@time: 2021/9/8 17:41
@desc: 给你一个整数数组 nums 和一个整数 target 。

向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
'''


def findTargetSumWays(nums, S: int) -> int:
    sumAll = sum(nums)
    if S > sumAll or (S + sumAll) % 2:
        return 0
    target = (S + sumAll) // 2

    dp = [0] * (target + 1)
    dp[0] = 1

    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] + dp[j - num]
    return dp[-1]

nums = [100]
target = -200
print(findTargetSumWays(nums, target))
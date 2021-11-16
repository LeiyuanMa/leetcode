# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: lengthOfLIS.py
@time: 2021/9/6 19:24
@desc: 最长递增序列（不连续）
'''


def lengthOfLIS(nums) -> int:
    size = len(nums)
    if size < 2:
        return size
    lst = [nums[0]]  # 定义保存最长子序列的数组

    for i in range(1, size):
        if nums[i] > lst[-1]:  # 如果比子序列最后一个数大，直接追加
            lst.append(nums[i])
            continue
        print(lst)

        l, r = 0, len(lst) - 1
        while l < r:  # 在已有的子序列数组中，用二分查找（该算法思路是组成数字最小的最长子序列，比如[10,9,2,5,3,7,101,18]，
                     # 示例中解释是[2,3,7,101]，但我们要找出的是[2,3,7,18]，找出最小的递增的数字来组合，最终长度都是一致的）
            mid = (l + r) // 2
            if lst[mid] >= nums[i]:  # 找出当前数字适合放入子序列的哪个位置（比子序列更大的直接追加了，因此这里找的是比子序列最后一个数要小的数的位置，
                                     # 比如子序列是[2,3,7]，现在来了一个nums[i] = 5，那么5就要把7给替换了，变成[2,3,5]）
                r = mid
            else:
                l = mid + 1
        lst[l] = nums[i]  # 找到合适的位置后替换成新的数字
    return len(lst)

nums = [10,9,2,5,3,4]
print(lengthOfLIS(nums))
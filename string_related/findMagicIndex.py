"""
魔术索引，满足条件A[i] = i
数组升序，且可能存在重复数据
"""
def findMagicIndex(nums):
    if not nums: return -1
    if nums[0] == 0: return 0
    p, n = 0, len(nums)
    while p < n:
        if nums[p] > p:
            p = nums[p]
        elif nums[p] == p:
            return p
        else:
            p += 1
    return -1


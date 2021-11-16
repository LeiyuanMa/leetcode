# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: findDuplicate.py
@time: 2021/9/6 20:13
@desc: 
'''

def findDuplicate(nums):
    """
    输入只有一个重复的数字
    """
    # size = len(nums)
    # for i in range(size):
    #     while nums[i] != i+1:   # 值不等于下标
    #         # 值是num[i]
    #         # 把值挪到对应的下标
    #         # 先把下标下的数存下来
    #         t = nums[nums[i]-1]
    #         if nums[nums[i]-1] == nums[i]:
    #             return nums[i]
    #         nums[nums[i]-1] = nums[i]
    #         nums[i] = t
    size = len(nums)
    for i in range(size):
        while i != nums[i]:
            t = nums[nums[i]]
            if t == nums[i]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            print(nums)

def findDisappearedNumbers(nums):
    res = list()
    for num in nums:
        if nums[abs(num)-1]>0:
            nums[abs(num)-1]*=-1
    for i, num in enumerate(nums):
        if num>0:
            res.append(i+1)
    return res


nums = [2, 3, 1, 0, 2, 5, 3]
print(findDuplicate(nums))
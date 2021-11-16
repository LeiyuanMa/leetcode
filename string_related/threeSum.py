# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: threeSum.py
@time: 2021/9/9 14:42
@desc: 
'''

def threeSum(nums):
    ans = list()
    size = len(nums)
    nums.sort()
    for i in range(size):
        j = i + 1
        k = size - 1
        while j < k:
            current_sum = nums[i] + nums[j] + nums[k]
            if current_sum == 0:
                if [nums[i], nums[j], nums[k]] not in ans:
                    ans.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
            elif current_sum < 0:
                j += 1
            else:
                k -= 1
    return ans


t=[-1,0,1,2,-1,-4,-2,-3,3,0,4]
print(threeSum(t))
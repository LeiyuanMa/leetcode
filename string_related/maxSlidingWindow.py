# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: maxSlidingWindow.py
@time: 2021/9/2 15:44
@desc: 仔细体会！！
'''

def maxSlidingWindow(nums, k: int):
    res = list()
    window = list()
    for i, num in enumerate(nums):
        if window and window[0] == i - k:
            window.pop(0)
        while window and nums[window[-1]] < num:
            window.pop()
        window.append(i)
        if i >= k - 1:
            res.append(nums[window[0]])
    return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maxSlidingWindow(nums, k))
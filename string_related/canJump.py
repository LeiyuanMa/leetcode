# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: canJump.py
@time: 2021/8/29 11:11
@desc: 
'''


def canJump(nums):
    max_i = 0  # 初始化当前能到达最远的位置
    for i, jump in enumerate(nums):  # i为当前位置，jump是当前位置的跳数
        if max_i >= i and i + jump > max_i:  # 如果当前位置能到达，并且当前位置+跳数>最远位置
            max_i = i + jump  # 更新最远能到达位置
        print(max_i)
        # 提前结束
        if max_i < i:
            return False
    return True

canJump([3,2,1,0,4])
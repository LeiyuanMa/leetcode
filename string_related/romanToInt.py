# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: romanToInt.py
@time: 2021/8/17 13:24
@desc:
'''


def romanToInt(s: str) -> int:
    mapping = {"I": 1,
               "V": 5,
               "X": 10,
               "L": 50,
               "C": 100,
               "D": 500,
               "M": 1000, }
    nums = len(s)
    result = 0
    for i in range(nums):
        if i < nums - 1 and mapping[s[i]] < mapping[s[i + 1]]:
            result -= mapping[s[i]]
        else:
            result += mapping[s[i]]
    return result

print(romanToInt("MCMXCIV"))
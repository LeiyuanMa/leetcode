# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: letterCombinations.py
@time: 2021/8/27 10:50
@desc: 
'''


def letterCombinations(digits: str):
    if not digits:
        return list()
    phoneMap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def backtrace(index):
        if index == len(digits):
            result.append("".join(combination))
        else:
            digit = digits[index]
            for t in phoneMap[digit]:
                combination.append(t)
                backtrace(index + 1)
                combination.pop()

    combination = list()
    result = list()
    backtrace(0)
    return result

t = "23"
print(letterCombinations(t))

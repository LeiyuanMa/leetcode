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

    def backtrace(index, combination):
        if index == len(digits):
            result.append("".join(combination))
            return
        else:
            digit = digits[index]
            for t in phoneMap[digit]:
                combination.append(t)
                backtrace(index + 1, combination)
                # 仔细想想要不要pop,显然ad,ae,af,a保持了不动，d,e,f是三种不同的组合，所以需要pop
                combination.pop()

    result = list()
    backtrace(0, list())
    return result

t = "23"
print(letterCombinations(t))

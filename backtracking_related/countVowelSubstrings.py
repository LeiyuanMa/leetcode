# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: countVowelSubstrings.py
@time: 2021/11/7 11:05
@desc: 统计字符串中的元音子字符串
'''


def countVowelSubstrings(word: str) -> int:
    setNum = {'a', 'e', 'i', 'o', 'u'}
    n = len(word)
    res = 0
    for i in range(n):
        for j in range(i + 5, n + 1):
            if set(word[i:j]) == setNum:
                res += 1
    return res

countVowelSubstrings("poazaeuioauoiioaouuouaui")
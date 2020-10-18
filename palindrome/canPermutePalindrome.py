"""
偶数长度的回文字符串所有的字符出现次数均为2
奇数长度的指由一个字符出现1次
"""
from collections import Counter

def canPermutePalindrome(s):
    count = [i for i in Counter(s).values() if i%2 == 1]
    return len(count) < 2



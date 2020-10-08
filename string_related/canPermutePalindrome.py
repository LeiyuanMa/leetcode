"""
偶数长度的回文字符串所有的字符出现次数均为2
奇数
"""
from collections import Counter

def canPermutePalindrome(s):
    count = [i for i in Counter(s).values() if i%2 == 1]
    return len(count) < 2

"""
给你一个字符串 s，它仅由字母 'a' 和 'b' 组成。每一次删除操作都可以从 s 中删除一个回文 "子序列"。
返回删除给定字符串中所有字符（字符串为空）的最小删除次数。
"""

def removePalindromeSub(s):
    if s == '':
        return 0
    elif s == s[::-1]:
        return 1  # 如果字符串是回文，直接全部删除即可。
    else:
        return 2  # 如果字符串不是回文，我们最多需要删两次。

if __name__ == "__main__":
    canPermutePalindrome("tactcoa")
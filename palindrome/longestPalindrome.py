# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: longestPalindrome.py
@time: 2021/8/25 21:57
@desc: 我们用 P(i,j) 表示字符串 s 的第 i 到 j 个字母组成的串（下文表示成 s[i:j]）是否为回文串
P(i,j)=P(i+1,j−1)∧(Si==Sj)

也就是说，只有 s[i+1:j-1]是回文串，并且 s 的第 i 和 j 个字母相同时，s[i:j] 才会是回文串。

'''


def longestPalindrome(s: str) -> str:
    n = len(s)
    if n < 2:
        return s

    max_len = 1
    begin = 0
    # dp[i][j] 表示 s[i..j] 是否是回文串
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True

    # 递推开始
    # 先枚举子串长度
    for L in range(2, n + 1):
        # 再枚举左边界
        for i in range(n):
            # 计算右边界
            j = L + i - 1

            if j >= n:
                break

            if s[i] != s[j]:
                dp[i][j] = False
            else:
                if L <= 2:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]

            if dp[i][j] and L > max_len:
                max_len = L
                begin = i
    return s[begin:begin + max_len]


s = "cbbd"
print(longestPalindrome(s))
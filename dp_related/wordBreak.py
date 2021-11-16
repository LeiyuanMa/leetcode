# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: wordBreak.py
@time: 2021/8/29 22:17
@desc: 
'''

def wordBreak(s, word_dict):
    dp = [False]*(len(s)+1)
    dp[0] = True
    for j in range(1, len(s)+1):
        for i in range(0,j):
            if dp[i] == True and s[i:j] in word_dict:
                dp[j] = True
                break
    return dp[-1]

s = "leetcode"
wordict = {"leet", "code"}
wordBreak(s,wordict)
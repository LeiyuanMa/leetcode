# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: longestWord.py
@time: 2021/11/9 23:04
@desc: 
'''

def longestWord(words):
    words.sort(key = lambda x:(-len(x), x))

    def dfs(w, words):
        if not w:
            return True
        for i, nxt in enumerate(words):
            if nxt == w[:len(nxt)]:
                if dfs(w[len(nxt):], words):
                    return True
        return False

    for i, word in enumerate(words):
        if dfs(word, words[i+1:]):
            return word
    return ""

words = ["cat","banana","dog","nana","walk","walker","dogwalker"]
print(longestWord(words))
# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: decodeString.py
@time: 2021/9/7 17:14
@desc: 
'''


def decodeString(s: str) -> str:
    stack = list()
    res = ""
    num = 0
    for ss in s:
        if '0' <= ss <= "9":
            num = int(ss)
        elif ss == "[":
            stack.append((num, res))
            res = ""
            num = 0
        elif ss == "]":
            current_num, current_res = stack.pop()
            res =  current_res + current_num * res
        else:
            res += ss
    return res

s= "3[a]2[bc]"
print(decodeString(s))
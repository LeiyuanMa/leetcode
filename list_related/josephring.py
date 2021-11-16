# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: josephring.py
@time: 2021/10/21 10:58
@desc: n个人，第m个人出列，最后一个出列的人的编号？
'''

def josephring(n,m):
    stack = list()
    for i in range(n):
        stack.append(i+1)

    index = m-1
    while stack:
        index%=len(stack)
        stack.pop(index)
        if len(stack)==1:
            return stack[0]
        index+=m-1
    return -1

print(josephring(10,17))
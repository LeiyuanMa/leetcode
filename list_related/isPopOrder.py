# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: isPopOrder.py
@time: 2021/10/21 11:25
@desc: 压栈序列1,2,3,4,5
        出栈序列可能是4,5,3,2,1
        不可能是4,3,5,1,2
'''

def isPopOrder(pushV, popV):
    if not pushV and len(pushV)!=len(popV):
        return False

    stack = list()
    index = 0
    for item in pushV:
        stack.append(item)
        while stack and stack[-1]==popV[index]:
            stack.pop()
            index+=1
    if not stack:
        return True
    else:
        return False

pushV = [1,2,3,4,5]
popV = [4,5,3,2,1]
print(isPopOrder(pushV,popV))
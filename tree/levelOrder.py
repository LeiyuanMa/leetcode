# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: levelOrder.py
@time: 2021/8/29 16:12
@desc: 
'''
class Node(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def levelOrder(root: Node):
    if not root:
        return list()
    stack = list()
    result = list()
    stack.append(root)
    while stack:
        current_level = list()
        for _ in range(len(stack)):
            tmp = stack.pop(0)
            print(tmp)
            current_level.append(tmp.val)
            if tmp.left:
                stack.append(tmp.left)
            if tmp.right:
                stack.append(tmp.right)
        result.append(current_level)
    return result

left_node = Node(1)
right = Node(4)
right.left = Node(3)
right.right = Node(6)
root = Node(5)
root.left = left_node
root.right = right
levelOrder(root)
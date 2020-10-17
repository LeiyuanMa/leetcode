# coding=utf-8
"""
二叉树的非递归遍历
参考https://zhuanlan.zhihu.com/p/261024283?utm_source=wechat_session
"""
class Node(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def preOrderTraversal(root):
    if not root:
        return
    temp = root
    stack = []
    result = []
    while temp or stack:
        while temp:
            stack.append(temp)
            result.append(temp.val)
            temp = temp.left
        if stack:
            temp = stack.pop()
            temp = temp.right
    return result

def inOrderTraversal(root):
    if not root:
        return
    temp = root
    stack = []
    result = []
    while temp or stack:
        while temp:
            stack.append(temp)
            temp = temp.left
        if stack:
            temp = stack.pop()
            result.append(temp.val)
            temp = temp.right
    return result

def postOrderTraversalV1(root):
    if not root:
        return
    temp = root
    stack = []
    result = []
    while temp or stack:
        while temp:
            result.append(temp.val)
            stack.append(temp)
            temp = temp.right
        if stack:
            temp = stack.pop()
            temp = temp.left
    result.reverse()
    return result

left_node = Node(2)
right = Node(3)
left_node.left = Node(4)
left_node.right = Node(5)

root = Node(1)
root.left = left_node
root.right = right

print(inOrderTraversal(root))

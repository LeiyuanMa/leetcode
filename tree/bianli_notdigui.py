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
            # 这里可以打印单一的子叶子节点
            temp, tmp_left = temp.right, temp.left
            if (not temp) ^ (not tmp_left):
                result.append(None)
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
            # 这里可以打印单一的子叶子节点
            temp,tmp_right = temp.left, temp.right
            if (not temp) ^ (not tmp_right):
                result.append(None)
    result.reverse()
    return result

left_node = Node(1)
right = Node(4)
right.left = Node(3)
right.right = Node(6)
root = Node(5)
root.left = left_node
root.right = right
print(inOrderTraversal(root))

# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: isValidBST.py
@time: 2021/11/14 9:26
@desc: 
'''


class TreeNode(object):
    """
    树定义
    """
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root):
    """
    判断是否二叉树
    """
    if not root:
        return True
    stack = list()
    tmp = root
    pre = float("-inf")
    while stack or tmp:
        while tmp:
            stack.append(tmp)
            tmp = tmp.left
        if stack:
            tmp = stack.pop()
            if tmp.val <= pre:
                return False
            pre = tmp.val
            tmp = tmp.right
    return True


root = TreeNode(1)
left = TreeNode(0)
right = TreeNode(2)
root.left = left
root.right = right
print(isValidBST(root))

# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: isValidBST.py
@time: 2021/8/29 15:52
@desc: 给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
'''
class Node(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def isValidBST(root: Node) -> bool:
    if not root:
        return True
    tmp = root
    stack = list()
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
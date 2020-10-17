"""
如果当前节点没有孩子，那我们不需要在节点后面加上任何括号；
如果当前节点只有左孩子，那我们在递归时，只需要在左孩子的结果外加上一层括号，而不需要给右孩子加上任何括号；
else:
如果当前节点只有右孩子，那我们在递归时，需要先加上一层空的括号 () 表示左孩子为空，再对右孩子进行递归，并在结果外加上一层括号。
如果当前节点有两个孩子，那我们在递归时，需要在两个孩子的结果外都加上一层括号；
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def tree2str(t):
    def func(node):
        if not node:
            return '()'
        l = func(node.left)
        r = func(node.right)
        if l == r == '()':
            return '('+ str(node.val) + ')'
        elif l != '()' and r == '()' :
            return '('+ str(node.val) + l + ')'
        else:
            return '('+ str(node.val) + l + r + ')'
    return func(t)[1:-1]

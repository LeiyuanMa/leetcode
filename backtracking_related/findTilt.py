# Definition for a binary tree node.
"""
给定一个二叉树，计算 整个树 的坡度。

一个树的 节点的坡度 定义即为，该节点左子树的结点之和和右子树结点之和的 差的绝对值 。空结点的的坡度是0。

整个树 的坡度就是其所有节点的坡度之和。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = 0

    def findTilt(self, root):
        self.helper(root)
        return self.res

    def helper(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val

        left = self.helper(root.left)
        right = self.helper(root.right)

        self.res += abs(left - right)
        return left + right + root.val


if __name__ == "__main__":
    left_node = TreeNode(2)
    right = TreeNode(3)
    left_node.left = TreeNode(4)
    left_node.right = TreeNode(5)

    root = TreeNode(1)
    root.left = left_node
    root.right = right
    obj = Solution()
    print(obj.findTilt(root))
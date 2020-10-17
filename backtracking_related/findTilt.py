# Definition for a binary tree node.
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
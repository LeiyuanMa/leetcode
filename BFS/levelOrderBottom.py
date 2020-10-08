"""
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
"""
def levelOrderBottom(root):
    res = []
    def dfs(root, depth):
        if not root:
            return
        if len(res)<depth+1:
            res.append([])
        res[depth].append(root.val)
        dfs(root.left, depth+1)
        dfs(root.right, depth+1)
    dfs(root,0)
    return res[::-1]
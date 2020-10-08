"""
二叉树的两个节点深度相同，但父节点不同，则它们是一对堂兄弟节点。
"""
def isCousins(root, x, y):
    parent = {}
    depth = {}
    def dfs(node, par = None):
        if node:
            depth[node.val] = 1 + depth[par.val] if par else 0
            parent[node.val] = par
            dfs(node.left, node)
            dfs(node.right, node)

    dfs(root)
    return depth[x] == depth[y] and parent[x] != parent[y]
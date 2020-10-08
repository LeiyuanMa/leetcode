"""
n叉树的最大深度
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        depth=1
        queue=[(root,depth)]
        while queue:
            root,depth=queue.pop(0)
            if root.children:
                # n叉数子节点是列表
                for node in root.children:
                    queue.append((node,depth+1))
        return depth
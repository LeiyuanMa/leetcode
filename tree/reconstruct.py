class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def construct_tree(pre_order, mid_order):
    # 忽略参数合法性判断
    if len(pre_order) == 0:
        return None
    # 前序遍历的第一个结点一定是根结点
    root_data = pre_order[0]
    i = mid_order.index(root_data)
    # 递归构造左子树和右子树
    left = construct_tree(pre_order[1: 1 + i], mid_order[:i])
    right = construct_tree(pre_order[1 + i:], mid_order[i + 1:])
    return Node(root_data, left, right)

def levelOrder(root):
    """
    普通二叉树层次遍历，并输出
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    res, level = [], [root]
    while root and level:
        currentNode = []
        nextLevel = []
        for node in level:
            currentNode.append(node.data)
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        res.append(currentNode)
        level = nextLevel
    return res

if __name__ == '__main__':
    pre_order = [3,9,20,15,7]
    mid_order = [9,3,15,20,7]
    root = construct_tree(pre_order, mid_order)
    t=1
    # print(levelOrder(root))
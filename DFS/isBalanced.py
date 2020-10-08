def isBalanced(root):
    def getDepth(node):
        if node == "NULL":
            return 0

        leftDepth = getDepth(node.left)
        if leftDepth == -1:
            return -1

        rightDepth = getDepth(node.right)
        if rightDepth == -1:
            return -1
        if abs(leftDepth - rightDepth) > 1:
            return -1
        else:
            return 1 + max(leftDepth, rightDepth)
    if getDepth(root) == -1:
        return False
    else:
        return True

"""
二叉树的多种遍历方式
参考自https://www.cnblogs.com/lliuye/p/9143676.html
"""
import collections

class Node(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class tree(object):
    def PreOrder(self, root):
        '''打印二叉树(先序)'''
        if root == None:
            return
        print(root.val, end=' ')
        self.PreOrder(root.left)
        self.PreOrder(root.right)

    def InOrder(self, root):
        '''中序打印'''
        if root == None:
            return
        self.InOrder(root.left)
        print(root.val, end=' ')
        self.InOrder(root.right)

    def BacOrder(self, root):
        '''后序打印'''
        if root == None:
            return
        self.BacOrder(root.left)
        self.BacOrder(root.right)
        print(root.val, end=' ')

    def BFS(self, root):
        '''广度优先(层次遍历)
        利用队列，依次将根，左子树，右子树存入队列，按照队列的先进先出规则来实现层次遍历。
        '''
        if root == None:
            return
        # queue队列，保存节点
        queue = []
        queue.append(root)

        while queue:
            # 拿出队首节点
            currentNode = queue.pop(0)
            # vals.append(currentNode.val)
            print(currentNode.val, end=' ')
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

    def DFS(self, root):
        '''深度优先
        利用栈，先将根入栈，再将根出栈，并将根的右子树，左子树存入栈，按照栈的先进后出规则来实现深度优先遍历。
        '''
        if root == None:
            return
        # 栈用来保存未访问节点
        stack = []
        stack.append(root)

        while stack:
            # 拿出栈顶节点
            currentNode = stack.pop()
            print(currentNode.val, end=' ')
            if currentNode.right:
                stack.append(currentNode.right)
            if currentNode.left:
                stack.append(currentNode.left)

    def maxDepth(self, root):
        '''深度优先
        利用栈，先将根入栈，再将根出栈，并将根的右子树，左子树存入栈，按照栈的先进后出规则来实现深度优先遍历。
        '''
        if root == None:
            return
        # 栈用来保存未访问节点
        stack = []
        stack.append(root)
        level = 0
        while stack:
            n = len(stack)
            for i in range(n):
                # 拿出栈顶节点
                currentNode = stack.pop(0)
                print(currentNode.val, end=' ')
                if currentNode.right:
                    stack.append(currentNode.right)
                if currentNode.left:
                    stack.append(currentNode.left)
            level += 1
        print("level",level)

def isSameTree(p, q):
    """
    判断俩棵树是否相同
    """
    if not p and not q:
        return True
    if not p or not q:
        return False

    queue1 = collections.deque([p])
    queue2 = collections.deque([q])

    while queue1 and queue2:
        node1 = queue1.popleft()
        node2 = queue2.popleft()
        if node1.val != node2.val:
            return False
        left1, right1 = node1.left, node1.right
        left2, right2 = node2.left, node2.right
        # 相同为0，不同为1，这里的用法很神奇
        if (not left1) ^ (not left2):
            return False
        if (not right1) ^ (not right2):
            return False
        if left1:
            queue1.append(left1)
        if right1:
            queue1.append(right1)
        if left2:
            queue2.append(left2)
        if right2:
            queue2.append(right2)

    return not queue1 and not queue2

left_node = Node(2)
right = Node(3)
left_node.left = Node(4)
right.right = Node(5)

a = Node(1)
a.left = left_node
a.right = right

b = Node(1)
b.left = left_node
b.right = right

# print(isSameTree(a,b))
obj = tree()
print(obj.DFS(a))
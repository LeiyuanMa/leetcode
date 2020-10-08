"""
二叉树的多种遍历方式
参考自https://www.cnblogs.com/lliuye/p/9143676.html
"""
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
        '''广度优先'''
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
        '''深度优先'''
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
"""
用两个栈实现一个队列
参考https://www.cnblogs.com/springionic/p/10576155.html
"""
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        if self.stack1 == []:
            return None
        else:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            out = self.stack2.pop()
            for j in range(len(self.stack2)):
                self.stack1.append(self.stack2.pop())
            return out
"""
用两个栈实现一个队列
参考https://www.cnblogs.com/shengguorui/p/11414676.html
"""
class Solution:
    def __init__(self):
        self.queueA=[]
        self.queueB=[]
    def push(self, node):
        self.queueA.append(node)
    def pop(self):
        if len(self.queueA)==0:
            return None
        while len(self.queueA)!=1:
            self.queueB.append(self.queueA.pop(0))
        self.queueA,self.queueB=self.queueB,self.queueA #交换是为了下一次的pop
        return self.queueB.pop()
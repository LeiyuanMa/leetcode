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
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result=[]
        while(matrix):
            result+=matrix.pop(0)
            if not matrix or not matrix[0]:
                break #if防止越界
            matrix=self.turn(matrix)
        return result
    def turn(self,matrix):
        nrow=len(matrix)
        ncol=len(matrix[0])
        newMatrix=[]
        for i in range(ncol):
            sb=[]
            for j in range(nrow):
                sb.append(matrix[j][i]) #取矩阵的每列第j行
            newMatrix.append(sb)
        newMatrix.reverse()#翻转
        return newMatrix


if __name__ == "__main__":
    matrix = [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,16]]
    sol = Solution()
    print(sol.printMatrix(matrix))
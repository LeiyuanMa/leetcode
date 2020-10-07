"""
给定一个数据和任意俩个下标，返回下标间元素的总和
前缀和！！
"""
class NumArray:
    def __init__(self, nums):
        self.num_sum = [0,]
        for i in range(len(nums)):
            self.num_sum.append(self.num_sum[i]+nums[i])

    def sumRange(self, i, j):
        return self.num_sum[j+1] - self.num_sum[i]

if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    result = obj.sumRange(0,2)
    print(result)
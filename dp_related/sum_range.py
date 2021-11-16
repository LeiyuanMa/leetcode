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

def productExceptSelf(nums):
    """
    除自己以外的数组乘积
    """
    length = len(nums)
    l = list()
    r = list()
    l.append(1)
    for i in range(1, length):
        l.append(l[i-1]*nums[i-1])
    print(l)
    for i in range(length-1, -1, -1):
        if i == length-1:
            r.append(1)
        else:
            r.append(r[-1]*nums[i+1])
    rr = r[::-1]
    print(rr)
    result = list()
    for i in range(length):
        result.append(l[i]*rr[i])
    return result



if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    # result = obj.sumRange(2,4)
    # print(result)
    print(productExceptSelf([1,2,3,4]))
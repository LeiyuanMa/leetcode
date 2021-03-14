class NumArray:

    def __init__(self, nums):
        self.adds = [0]
        add = 0
        for i in range(len(nums)):
            add += nums[i]
            self.adds.append(add)
        print(self.adds)

    def sumRange(self, i: int, j: int) -> int:
        return self.adds[j + 1] - self.adds[i]


obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0,3))
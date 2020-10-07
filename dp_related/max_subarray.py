"""
 连续子数组的最大和
 当 dp[i - 1] > 0 时：执行 dp[i] = dp[i-1] + nums[i]；
 当 dp[i−1]≤0 时：执行 dp[i] = nums[i] ；
 初始状态： dp[0] = nums[0]
"""
def maxSubArray( nums):
    for i in range(1, len(nums)):
        nums[i] += max(nums[i - 1], 0)
    return max(nums)

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result = maxSubArray(nums)
    print(result)
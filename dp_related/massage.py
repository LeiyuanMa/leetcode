"""
 dp 数组多设置一行，相应地定义就要改变，遍历的一些细节也要相应改变
 dp[i][0]：区间 [0, i) 里接受预约请求，并且下标为 i 的这一天不接受预约的最大时长
 dp[i][1]：区间 [0, i) 里接受预约请求，并且下标为 i 的这一天接受预约的最大时长
"""
import numpy as np
def massage(nums):
    length = len(nums)
    dp = np.zeros((length+1,2))
    for i in range(1,length+1):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
        dp[i][1] = dp[i - 1][0] + nums[i - 1]
    return max(dp[length][0], dp[length][1])

if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    result = massage(nums)
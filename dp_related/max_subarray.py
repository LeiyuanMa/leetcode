"""
 连续子数组的最大和
 当 dp[i - 1] > 0 时：执行 dp[i] = dp[i-1] + nums[i]；
 当 dp[i−1]≤0 时：执行 dp[i] = nums[i] ；
 初始状态： dp[0] = nums[0]
"""
def maxSubArray(nums):
    for i in range(1, len(nums)):
        nums[i] += max(nums[i - 1], 0)
    return max(nums)


def maxProduct(nums):
    min_p, max_p, res = nums[0], nums[0], nums[0]
    for n in nums[1:]:
        cur_min = min(min_p * n, max_p * n, n)
        cur_max = max(min_p * n, max_p * n, n)
        res = max(res, cur_max)
        # 坑了一把，注意要先保存再赋值，不然会影响当前最大最小值的计算
        min_p = cur_min
        max_p = cur_max
    return res


def corpFlightBookings(bookings, n):
    """
    差分数组
    """
    nums = [0] * n
    for left, right, inc in bookings:
        nums[left - 1] += inc
        if right < n:
            nums[right] -= inc
    print(nums)

    for i in range(1, n):
        nums[i] += nums[i - 1]

    return nums


if __name__ == "__main__":
    nums = [2,3,-2,4]
    # result = maxSubArray(nums)
    result = maxProduct(nums)
    # bookings = [[1,2,10],[2,3,20],[2,5,25]]
    # n = 5
    # result =corpFlightBookings(bookings, n)
    # print(result)
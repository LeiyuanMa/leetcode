"""
每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
"""
def minCostClimbingStairs(cost):
    size = len(cost)
    dp = [0 for _ in range(size)]

    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, size):
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

    return min(dp[size - 1], dp[size - 2])

if __name__ == "__main__":
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    minCostClimbingStairs(cost)
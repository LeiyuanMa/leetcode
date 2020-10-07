"""
有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。
结果可能很大，你需要对结果模1000000007。
"""
def waysToStep(n):
    if n < 3:
        return n  #入口参数检查
    dp = [0 for i in range(n + 1)]
    dp[1], dp[2], dp[3] = 1, 2, 4
    for i in range(4, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000007
    return dp[n]

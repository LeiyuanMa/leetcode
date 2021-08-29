# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: longestCommonSubsequence.py
@time: 2021/8/8 18:31
@desc: 最长公共子序列的长度
可以定义 dp[i][j] 表示 text1[0:i-1] 和 text2[0:j-1] 的最长公共子序列。
 （注：text1[0:i-1] 表示的是 text1 的 第 0 个元素到第 i - 1 个元素，两端都包含）
之所以 dp[i][j] 的定义不是 text1[0:i] 和 text2[0:j] ，是为了方便当 i = 0 或者 j = 0 的时候，
dp[i][j]表示的为空字符串和另外一个字符串的匹配，这样 dp[i][j] 可以初始化为 0.

2. 状态转移方程
知道状态定义之后，我们开始写状态转移方程。

当 text1[i - 1] == text2[j - 1] 时，说明两个子字符串的最后一位相等，
所以最长公共子序列又增加了 1，所以 dp[i][j] = dp[i - 1][j - 1] + 1；
举个例子，比如对于 ac 和 bc 而言，他们的最长公共子序列的长度等于 a 和 b 的最长公共子序列长度 0 + 1 = 1。
当 text1[i - 1] != text2[j - 1] 时，说明两个子字符串的最后一位不相等，
那么此时的状态 dp[i][j] 应该是 dp[i - 1][j] 和 dp[i][j - 1] 的最大值。
举个例子，比如对于 ace 和 bc 而言，他们的最长公共子序列的长度等于 ① ace 和 b 的最长公共子序列长度0
与 ② ac 和 bc 的最长公共子序列长度1 的最大值，即 1。
综上状态转移方程为：

dp[i][j] = dp[i - 1][j - 1] + 1dp[i][j]=dp[i−1][j−1]+1, 当 text1[i - 1] == text2[j - 1];text1[i−1]==text2[j−1];
dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])dp[i][j]=max(dp[i−1][j],dp[i][j−1]), 当 text1[i - 1] != text2[j - 1]text1[i−1]!=text2[j−1]
'''

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        M, N = len(text1), len(text2)
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[M][N]
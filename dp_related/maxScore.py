"""
给你一个由若干 0 和 1 组成的字符串 s ，请你计算并返回将该字符串分割成两个 非空 子字符串（即 左 子字符串和 右 子字符串）所能获得的最大得分。

「分割字符串的得分」为 左 子字符串中 0 的数量加上 右 子字符串中 1 的数量。
"""
def maxScore(s):
    res = 0
    cur = s.count('1')  # 初始化
    # cur = sum([1 for char in s if char == '1'])     # 不知道上面那个API的可以用这个
    for char in s[:-1]:     # 需要排除最后一个字符串，否则与题意【分割成两个非空子字符串】矛盾
        cur = cur - 1 if char == '1' else cur + 1       # 状态转移
        res = max(res, cur)     # 更新结果
    return res

if __name__ == "__main__":
    print(maxScore("011101"))
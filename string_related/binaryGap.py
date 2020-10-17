"""
给定一个正整数 n，找到并返回 n 的二进制表示中两个 相邻 1 之间的 最长距离 。如果不存在两个相邻的 1，返回 0 。
"""


def binaryGap(N) -> int:
    tmp = bin(N)[2:]
    n = []
    for i, v in enumerate(tmp):
        if v == '1':
            n.append(i)
    res = 0
    for i in range(len(n) - 1):
        res = max(res, n[i + 1] - n[i])
    return res

if __name__ == "__main__":
    a = 22

    print(binaryGap(a))
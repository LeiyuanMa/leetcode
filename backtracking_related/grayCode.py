def grayCode(n):
    """
    格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
    """
    if n == 0:
        return [0]

    res = []

    def back(now, x):
        if len(now) == n:
            res.append(int(now, 2))
        elif x == 0:
            back(now + '0', 0)
            back(now + '1', 1)
        else:
            back(now + '1', 0)
            back(now + '0', 1)

    back('', 0)
    return res


if __name__ == "__main__":
    print(grayCode(2))
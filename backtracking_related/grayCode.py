def grayCode(n):
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
            back(now + '0', 0)
            back(now + '1', 1)

    back('', 0)
    return res


if __name__ == "__main__":
    print(grayCode(2))
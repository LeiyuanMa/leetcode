def isAdditiveNumber(num):
    """
    | n1 | n2 | ....
    0    i    j
    两个分界点，分别用i和j来表示。

    :param num:
    :return:
    """
    if len(num) < 3:
        return False

    def backtrack(n1, n2, r):
        """
        开始回溯。
        :param n1: 第一个数字。
        :param n2: 第二个数字。
        :param r: 剩下的数字。
        :return:
        """
        s = str(int(n1) + int(n2))
        if s == r:
            return True
        elif len(s) > len(r) or r[:len(s)] != s:
            return False
        else:
            return backtrack(n2, s, r[len(s):])

    for i in range(1, len(num) + 1):  # 找到第一个数：num[:i]
        for j in range(i + 1, len(num)):  # 找到第二个数：num[i:j]
            num1, num2, rest = num[:i], num[i:j], num[j:]
            if backtrack(num1, num2, rest):
                return True
    return False


if __name__ == "__main__":
    num = "112358"
    print(isAdditiveNumber(num))

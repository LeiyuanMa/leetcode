def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    res = 10
    k = 9
    temp = 9
    # python的range函数天然不包括上限，因此都加1
    upper = min(n+1, 11)
    for i in range(2, upper):
        temp *= k
        k -= 1
        res += temp

    return res

if __name__ == "__main__":
    print(countNumbersWithUniqueDigits(2))
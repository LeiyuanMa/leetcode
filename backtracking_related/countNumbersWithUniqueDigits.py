"""
给一个非负整数n,找出[0,10^)之间各个位上数字不重复出现的数的个数，
如n = 3，找出[0，1000）之间符合标准的数，如123，245，但122不符合要求，2重复出现。
"""
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
    print(countNumbersWithUniqueDigits(3))
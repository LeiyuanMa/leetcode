"""
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数
对于二位数ab=a*10+b：
ab%9=(10*a+b)%9=(a+b)%9
对于三位数abc=a*100+10*b+c：
abc%9=(a+b+c)%9
对于一般整数来说直接对整数进行对9求余，便可得到小于10的结果。
而对于整除结果，如18，正确结果为9，而按上述规则则为0，所以不适用，通过规律可得，除0以外，能被9整除的数各位相加后其值最终为9（因为各位数相加后始终能被9整除）
"""


def addDigits(num):
    if num == 0:
        return 0
    if num % 9 == 0:
        return 9
    else:
        return num % 9

if __name__ == "__main__":
    a = 101

    print(addDigits(a))
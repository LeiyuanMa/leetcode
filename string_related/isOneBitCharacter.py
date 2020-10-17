"""
有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。

现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。
"""
def isOneBitCharacter(bits):
    i = 0
    while i < len(bits)-1:
        if bits[i] == 1:
            i += 2
        else:
            i += 1
    return i == len(bits)-1

if __name__ == "__main__":
    bits = [1, 1, 1, 0]
    print(isOneBitCharacter(bits))

def convertInteger(A: int, B: int) -> int:
    res = 0
    c = A ^ B
    for i in range(32):
        res += c >> i & 1
    return res




if __name__ == "__main__":
    a = 1
    b = 2
    print(convertInteger(a,b))
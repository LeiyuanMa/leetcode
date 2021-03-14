def add(a,b):
    while b != 0:
        sum = a ^ b
        carry = (a&b) << 1
        a = sum
        b = carry
    return a

if __name__ == "__main__":
    a = 11
    b = 3

    print(add(a,b))
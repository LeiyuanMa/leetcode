"""
模拟加法，实现二进制求和（多进制）
"""
def addBinary(a, b):
    if not a or not b:
        return a or b

    a, b, ans = a[::-1], b[::-1], []
    # carry: 进位
    i = j = carry = 0
    while i < len(a) or j < len(b) or carry:
        n1 = int(a[i]) if i < len(a) else 0
        n2 = int(b[j]) if j < len(b) else 0
        carry, cur = divmod(n1 + n2 + carry, 2)
        ans.append(str(cur))
        i, j = i + 1, j + 1
    return ''.join(ans[::-1])


if __name__ == "__main__":
    a = "11"
    b = "1"
    print(addBinary(a,b))
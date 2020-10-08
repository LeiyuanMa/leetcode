"""
给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false 。
必须交换一次，即使A==B也有可能并不满足要求
"""
def buddyStrings(A, B):
    if len(A) != len(B):
        return False
    if A == B:
        seen = set()
        for a in A:
            if a in seen:
                return True
            seen.add(a)
        return False
    else:
        pairs = []
        for a, b in zip(A, B):
            if a != b:
                pairs.append((a, b))
            if len(pairs) >= 3:
                return False
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]


if __name__ == "__main__":
    a = "ab"
    b = "ba"
    print(buddyStrings(a,b))
"""
给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。
"""
def maxPower(s) -> int:
    left, right = 0, 0
    res = 1  # 长度最短为1
    while left <= right < len(s):
        if s[left] == s[right]:
            right += 1
            res = max(res, right - left)
        else:
            left = right
    return res


if __name__ == "__main__":
    s = "leetcode"
    print(maxPower(s))
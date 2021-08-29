def countAndSay(n):
    if n == 1:
        return '1'
    s = countAndSay(n - 1)

    i, res = 0, ''
    for index, current_value in enumerate(s):
        if current_value != s[i]:
            res += str(index - i) + s[i]
            i = index
    res += str(len(s) - i) + s[-1]  # 最后一个元素莫忘统计
    return res

print(countAndSay(5))
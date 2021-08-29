def maxlengthofSubstring(s):
    max_len = 0
    # dic{当前字符， 当前字符的位置}
    dic = {}
    flag_len = 0
    start = 0
    if s is None or len(s) == 0:
        return 0
    for i in range(len(s)):
        if (s[i] in dic and dic[s[i]] > start):
            start = dic[s[i]] + 1
            print("start",start)
        flag_len = i - start + 1
        dic[s[i]] = i
        max_len = max(max_len, flag_len)
        print(dic, start, max_len)
    return max_len

print(maxlengthofSubstring("abcabcbb"))
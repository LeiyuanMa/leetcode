"""
二分查找法寻找最长公共前缀:
最长公共前缀的长度不会超过字符串数组中的最短字符串的长度。
"""
def longestCommonPrefix(strs):
    def isCommonPrefix(length):
        # 取任意一个字符串的前length个元素即可，如果是公共的话，所有字符串的都一致
        str0, count = strs[0][:length], len(strs)
        return all(strs[i][:length] == str0 for i in range(1, count))

    if not strs:
        return ""

    minLength = min(len(s) for s in strs)
    low, high = 0, minLength
    while low < high:
        mid = (high - low + 1) // 2 + low
        if isCommonPrefix(mid):
            low = mid
        else:
            high = mid - 1

    return strs[0][:low]

if __name__ == "__main__":
    print(longestCommonPrefix(["flower","flow","flight"]))
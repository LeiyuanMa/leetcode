"""
二分查找法寻找最长公共前缀:
最长公共前缀的长度不会超过字符串数组中的最短字符串的长度。
"""
# def longestCommonPrefix(strs):
#     def isCommonPrefix(length):
#         # 取任意一个字符串的前length个元素即可，如果是公共的话，所有字符串的都一致
#         str0, count = strs[0][:length], len(strs)
#         return all(strs[i][:length] == str0 for i in range(1, count))
#
#     if not strs:
#         return ""
#
#     minLength = min(len(s) for s in strs)
#     low, high = 0, minLength
#     while low < high:
#         mid = (high - low + 1) // 2 + low
#         if isCommonPrefix(mid):
#             low = mid
#         else:
#             high = mid - 1
#
#     return strs[0][:low]
def longestCommonPrefix(strs) -> str:
    max_len = min([len(s) for s in strs])
    i = 1
    ans = "" if len(strs) > 1 else strs[0]
    while i <= max_len:
        common_str = strs[0][:i]
        if all([s[:i] == common_str for s in strs[1:]]):
            ans = common_str
        i += 1
    return ans

if __name__ == "__main__":
    print(longestCommonPrefix(["ab","a"]))
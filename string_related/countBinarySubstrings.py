"""
00110011
2222(2个0,2个1,2个0,2个1)
----->0011,  1100,   0011
        01,    10,    01
"""
# def countBinarySubstrings(s):
#     ptr = 0
#     n = len(s)
#     last = 0
#     ans = 0
#     while (ptr < n) :
#         c = s[ptr]
#         count = 0
#         while (ptr < n and s[ptr] == c):
#             ptr+=1
#             count+=1
#         ans += min(count, last)
#         last = count
#
#     return ans
def countBinarySubstrings(s):
    nums = []
    i = 0
    for j, c in enumerate(s):
        if c != s[i]:
            nums.append(j-i)
            i = j
    nums.append(len(s) - i)
    res = 0
    for i in range(1, len(nums)):
        res += min(nums[i-1], nums[i])
    return res

if __name__ == "__main__":
    s = "11001100"
    print(countBinarySubstrings(s))


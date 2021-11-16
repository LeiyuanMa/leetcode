"""
长度为n的字符串中字典序第K小的开心字符串

开心字符串，s[i+1]!=s[i], 仅包含a b c
"""

def getHappyString(n, k):
    res = []

    def dfs(curr, temp):
        if len(curr) == n:
            res.append(curr)
            return
        for t in temp:
            new = [c for c in ['a', 'b', 'c'] if c != t]
            dfs(curr + t, new)

    dfs('', ['a', 'b', 'c'])
    print(res)
    return res[k - 1] if k - 1 < len(res) else ''

if __name__ == "__main__":
    print(getHappyString(2, 3))
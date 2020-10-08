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
def maxUniqueSplit(s):
    res = 1

    def dfs(hm={}, fr=0, to=1):  # 从fr到to进行分段
        nonlocal res
        if to > len(s):
            res = max(res, len(hm.keys()))  # len(hm.keys())已经分段的字串数量
            return
        elif len(hm.keys()) + len(s) - fr <= res:  # 减枝: 显然剩余的再怎么分都不可能搜到新的最大字串数
            return

        piece = s[fr: to]  # 当前准备拆分的子串

        if piece not in hm:
            hm[piece] = 1  # 标记已分段的子串
            dfs(hm, to, to + 1)  # 表示进行分段，则进行状态的转移 -> fr':=to
            hm.pop(piece)  # 撤销哈希状态
        dfs(hm, fr, to + 1)  # 已经重复则不分段

    dfs()
    return res

if __name__ == "__main__":
    print(maxUniqueSplit("ababccc"))
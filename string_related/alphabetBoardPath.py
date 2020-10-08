"""
https://leetcode-cn.com/problems/alphabet-board-path/
为了避免Z的位置出界，到达Z的时候，优先往左L，从Z出发优先往上U
"""
def alphabetBoardPath(target):
    x, y, d = 0, 0, dict()
    for i in range(26):
        d[chr(i + 97)] = (i // 5, i % 5)
    cur, ans = (0, 0), []
    for c in target:
        nxt = d[c]
        dx, dy = nxt[0] - cur[0], nxt[1] - cur[1]
        if dx < 0: ans += ['U'] * (-dx)
        if dy < 0: ans += ['L'] * (-dy)
        if dx > 0: ans += ['D'] * dx
        if dy > 0: ans += ['R'] * dy
        ans.append('!')
        cur = nxt
    return ''.join(ans)


if __name__ == "__main__":
    print(alphabetBoardPath("leetzt"))
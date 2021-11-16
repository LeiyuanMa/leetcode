# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: numIslands.py
@time: 2021/9/1 22:17
@desc: 最大岛屿面积和岛屿数量
'''


def numIslands(grid) -> int:
    m = len(grid)
    n = len(grid[0])
    taken = [[0] * n for _ in range(m)]
    num = 0
    max_area = 0
    global area
    direction = [[0, 1], [0, -1], [-1, 0], [1, 0]]

    def dfs(i, j):
        for dx, dy in direction:
            ix = i + dx
            iy = j + dy
            if 0 <= ix < m and 0 <= iy < n and int(grid[ix][iy]) > 0 and taken[ix][iy] == 0:
                taken[ix][iy] = 1
                global area
                area += 1
                dfs(ix, iy)

        return

    for i in range(m):
        for j in range(n):
            if int(grid[i][j]) > 0 and taken[i][j] == 0:
                num += 1
                area = 1
                taken[i][j] = 1
                dfs(i, j)
            if area > max_area:
                max_area = area
    print(max_area)
    return num


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(numIslands(grid))
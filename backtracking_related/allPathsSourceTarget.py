"""
给一个有 n 个结点的有向无环图，找到所有从 0 到 n-1 的路径并输出（不要求按顺序）

二维数组的第 i 个数组中的单元都表示有向图中 i 号结点所能到达的下一些结点
（译者注：有向图是有方向的，即规定了 a→b 你就不能从 b→a ）空就是没有下一个结点了。
"""
def allPathsSourceTarget(graph):
    N = len(graph)

    def solve(node):
        if node == N-1:
            return [[N-1]]
        ans = []
        for nei in graph[node]:
            for path in solve(nei):
                ans.append([node] + path)
        return ans

    return solve(0)

if __name__ == "__main__":
    graph = [[1, 2], [3], [3], []]
    print(allPathsSourceTarget(graph))
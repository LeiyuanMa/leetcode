def countNegatives(grid):
    total = 0
    i, j = 0, len(grid[0])-1

    while i < len(grid) and j>=0:
        if grid[i][j] >= 0:
            i += 1
        else:
            total += len(grid) - i
            j -= 1
    return total

if __name__ == "__main__":
    grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    countNegatives(grid)
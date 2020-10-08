def floodFill( image, sr, sc, newColor):
    def draw(sr, sc):
        # 要填充的点必须在图像内, 并且与旧的颜色相同, 并且与新的颜色不同(避免往回填充)
        if 0 <= sr < len(image) and 0 <= sc < len(image[0]) and image[sr][sc] == oldColor and image[sr][sc] != newColor:
            image[sr][sc] = newColor # 填充当前点
            # 对上下左右四个点递归
            draw(sr+1, sc)
            draw(sr-1, sc)
            draw(sr, sc+1)
            draw(sr, sc-1)
    oldColor = image[sr][sc]
    draw(sr, sc)
    return image

if __name__ == "__main__":
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    print(floodFill(image, sr,sc, newColor))
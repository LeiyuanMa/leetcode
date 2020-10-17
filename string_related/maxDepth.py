def maxDepth(s):
    count = 0
    res = []
    for str in s:

        if str == "(":
            count += 1
            res.append(count)
        if str == ")":
            count -= 1
    return max(res)

if __name__ == "__main__":
    s = "(1+(2*3)+((8)/4))+1"
    print(maxDepth(s))

def GetUglyNumber_Solution(index):
    # write code here
    #如果为空则返回0
    #如果不为空则通过索引判断是否为丑数
    if index <=0:
        return 0
    res = [1]
    index2 = index3 = index5 = 0
    for i in range(1, index):
        u2 = res[index2] * 2
        u3 = res[index3] * 3
        u5 = res[index5] * 5
        res.append(min(u2, min(u3, u5)))
        print(res)
        if res[i]/2 == res[index2]:
            index2 += 1
        if res[i]/3 == res[index3]:
            index3 += 1
        if res[i]/5 == res[index5]:
            index5 += 1
    return res.pop()


print(GetUglyNumber_Solution(20))
"""
参考于：https://zhuanlan.zhihu.com/p/84759645
"""
def shell_sort(numberlist):
    length = len(numberlist)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            temp = numberlist[i]
            j = i
            while j >= gap and numberlist[j - gap] > temp:
                numberlist[j] = numberlist[j - gap]
                j -= gap
            numberlist[j] = temp
        gap = gap // 2
    return numberlist

if __name__ == "__main__":
    nums = [5,3,7,2,4,1,8]
    shell_sort(nums)
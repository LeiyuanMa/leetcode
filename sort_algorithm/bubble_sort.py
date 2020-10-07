"""
参考于：https://zhuanlan.zhihu.com/p/84759645
"""
def bubble_sort(numberlist):
    length = len(numberlist)
    for i in range(length):
        for j in range(1, length - i):
            if numberlist[j - 1] > numberlist[j]:
                numberlist[j], numberlist[j - 1] = numberlist[j - 1], numberlist[j]
    return numberlist

if __name__ == "__main__":
    nums = [3,5,7,2,4,1,8]
    bubble_sort(nums)
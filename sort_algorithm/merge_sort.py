"""
参考于：https://zhuanlan.zhihu.com/p/84759645
增加了逆序数的计算
"""
nixushu = 0
def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            global nixushu
            nixushu = nixushu + len(left)
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result

def merge_sort(numberlist):
    if len(numberlist) <= 1:
        return numberlist
    mid = len(numberlist) // 2
    left = numberlist[:mid]
    right = numberlist[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

if __name__ == "__main__":
    nums = [5,3,7,2,4,1,8]
    merge_sort(nums)
    print(nixushu)
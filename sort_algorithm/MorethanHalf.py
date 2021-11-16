#O(n)复杂度，
def function_partion(lists, left, right):
    """
    该方法返回一个index，能够保证index位置的数是已排序完成的，
    在index左边的数都比index所在的数小，在index右边的数都比index所在的数大。
    """
    # 划分函数处理部分
    key = lists[left]
    while left < right:
        # 把小于key的数挪到左边
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        # 把大于key的数挪到右边
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    return left


def MorethanHalf(lists):
    # 划分法主要函数部分
    length = len(lists)
    left = 0
    right = length - 1
    index = function_partion(lists, left, right)
    k = length // 2
    while k != index:
        if index > k :
            right = index - 1
        else:
            left = index + 1
        index = function_partion(lists, left, right)
    print(k,lists)
    return lists[k]

def GetLeastK(lists,k):
    # 划分法主要函数部分
    length = len(lists)
    left = 0
    right = length - 1
    index = function_partion(lists, left, right)
    # k-1是因为index从0开始
    while k-1 != index:
        if index > k-1 :
            right = index - 1
        else:
            left = index + 1
        index = function_partion(lists, left, right)
    print(lists[:k])



lists = [4,5,2,1,2,2,2,3]
print("思路(划分法):", MorethanHalf(lists))
# lists = [4,5,1,6,2,7,3,8]
# GetLeastK(lists,4)
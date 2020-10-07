"""
参考于：https://zhuanlan.zhihu.com/p/84759645
"""
def findSmallest(arr):  # 用于查找出数组中最小的元素，返回最小元素的索引。
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectSort(arr):
    newArr = []
    while arr:
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

if __name__ == "__main__":
    nums = [3,5,7,2,4,1,8]
    selectSort(nums)
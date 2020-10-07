"""
参考于：https://zhuanlan.zhihu.com/p/84759645
"""
def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

if __name__ == "__main__":
    nums = [5,3,7,2,4,1,8]
    quick_sort(nums)
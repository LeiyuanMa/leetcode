"""
参考于：https://zhuanlan.zhihu.com/p/84759645
"""
def insert_sort(data):
    for k in range(1, len(data)):
        cur = data[k]
        j = k
        while j > 0 and data[j - 1] > cur:
            data[j] = data[j - 1]
            j -= 1
        data[j] = cur
    return data

if __name__ == "__main__":
    nums = [3,5,7,2,4,1,8]
    insert_sort(nums)
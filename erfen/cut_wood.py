#给定数组，每个元素代表一个木头的长度，木头可以任意截断， 从这堆木头中截出至少k个相同长度为m的木块，已知k，求max(m)
import sys

def isfit(nums,k,mid):
    count = 0
    for num in nums:
        count += num//mid
    return count >= k

def maxM(nums,k):
    min_num = sys.maxsize
    max_num = -sys.maxsize-1
    for num in nums:
        min_num = min(num,min_num)
        max_num = max(num,max_num)

    ans = -1
    while min_num < max_num:
        mid = (min_num+max_num)//2
        if isfit(nums,k,mid):
            ans = mid
            min_num = mid +1
        else:
            max_num = mid -1

    return ans

if __name__ == "__main__":
    nums = [4,7,2,10,5]
    k=5
    print(maxM(nums,k))


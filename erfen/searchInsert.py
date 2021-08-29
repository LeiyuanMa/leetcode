def searchInsert(nums, target):
    left,right=0,len(nums)
    while left<right:
        mid=left+(right-left)//2
        if nums[mid]<target:
            left = mid+1
        else:
            right = mid
    return left


if __name__ == "__main__":
    s = [1,3,5,6]
    t = 5
    print(searchInsert(s,t))

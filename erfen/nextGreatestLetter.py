"""快手二面"""
def nextGreatestLetter(letters, target):
    length = len(letters)
    # 循环的特殊情况
    if letters[length - 1] <= target:
        return letters[0]
    left = 0
    right = length - 1
    while left < right:
        mid = (left + right) // 2
        letter = letters[mid]
        if letter == target:
            # 等于目标值，往右找
            left = mid + 1
        elif letter < target:
            # 比目标值小，往右找
            left = mid + 1
        else:
            # 比目标值大，可能就是要找的数！
            right = mid
    return letters[left]

def lengthOfLIS(nums):
    """
    最长递增子序列
    输入：nums = [10,9,2,5,3,7,101,18]
    输出：4
    解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
    """
    size = len(nums)
    if size == 1:
        return size

    ans = [nums[0]]
    for n in nums[1:]:
        # 严格递增
        if n > ans[-1]:
            ans.append(n)
            continue

        left, right = 0, len(ans)
        while left < right:
            mid = (left + right) // 2
            if ans[mid] >= n:
                right = mid
            else:
                left = mid + 1
        ans[left] = n
    return len(ans)

if __name__ == "__main__":
    letters = ["c", "f", "j"]
    target = "a"
    print(nextGreatestLetter(letters,target))
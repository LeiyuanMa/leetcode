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

if __name__ == "__main__":
    letters = ["c", "f", "j"]
    target = "a"
    nextGreatestLetter(letters,target)
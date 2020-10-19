def twoSum(numbers, target):
    i = 0
    j = len(numbers) - 1
    while i < j:
        if target - numbers[j] == numbers[i]:
            return [i + 1, j + 1]
        elif numbers[i] + numbers[j] > target:
            j -= 1
        else:
            i += 1
    return []


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    print(twoSum(numbers,target))
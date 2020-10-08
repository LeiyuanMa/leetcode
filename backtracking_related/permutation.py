def permutation(str,start,end):
    """
    数组的全排列
    :param str:
    :param start:
    :param end:
    :return:
    """
    if(start==end):
        for s in str:
            print(s,end='')
        print('')
        return
    for i in range(start,end):
        str[start],str[i]=str[i],str[start]
        permutation(str,start+1,end)
        str[start], str[i] = str[i], str[start]

def permuteUnique(nums):
    """
    含重复元素的数组的不重复全排列
    :param nums:
    :return:
    """
    nums.sort()
    res = []
    check = [0 for i in range(len(nums))]

    def backtrack(sol, nums, check):
        if len(sol) == len(nums):
            res.append(sol)
            return

        for i in range(len(nums)):
            if check[i] == 1:
                continue
            if nums[i] == nums[i - 1] and check[i - 1] == 0:
                continue
            check[i] = 1
            backtrack(sol + [nums[i]], nums, check)
            check[i] = 0

    backtrack([], nums, check)
    return res

def subsets(nums):
    """
    不含重复元素的数组的子集
    :param self:
    :param nums:
    :return:
    """
    if not nums:
        return []
    res = []
    n = len(nums)

    def helper(idx, temp_list):
        res.append(temp_list)
        for i in range(idx, n):
            helper(i + 1, temp_list + [nums[i]])

    helper(0, [])
    print(res)
    return res

def subsets_widthdup(nums):
    """
    含重复元素的数组的子集
    :param self:
    :param nums:
    :return:
    """
    if not nums:
        return []
    n = len(nums)
    res = []
    nums.sort()
    n = len(nums)

    def helper1(idx, temp_list):
        if temp_list not in res:
            res.append(temp_list)
        for i in range(idx, n):
            helper1(i + 1, temp_list + [nums[i]])

    helper1(0, [])
    print(res)
    return res

a=[1,2,2]
# permutation(a,0,len(a))
print(permuteUnique(a))
# subsets(a)
# subsets_widthdup(a)
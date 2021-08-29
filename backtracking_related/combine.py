def combine(n, k):
    """
    1-n的整数，返回长度为k组合数
    :param n:
    :param k:
    :return:
    """
    # 明显用回溯法:
    res = []
    #特殊情况处理
    if n == 0 or k == 0:
        return res
    #先生成数
    nums = [i for i in range(1,n+1)]

    def backtrace(curr_res,index):
        if len(curr_res)==k:
            res.append(curr_res[:]) ##浅拷贝，这一步很重要
            return

        for i in range(index,n):
            curr_res.append(nums[i])
            backtrace(curr_res,i+1)
            curr_res.pop()

    backtrace([],0)
    return res

def combinationSum(candidates, target):
    """
    无限制的使用数组里的数，和为target的组合数
    :param candidates:
    :param target:
    :return:
    """
    def dfs(candidates, begin, path, res, target):
        if target == 0:
            res.append(path)
            return

        for index in range(begin,size):
            if candidates[index] > target:
                continue
            dfs(candidates, index, path + [candidates[index]], res, target - candidates[index])

    size = len(candidates)
    if size == 0:
        return []
    path = []
    res = []
    dfs(candidates, 0, path, res, target)
    return res

def combinationSum2(candidates, target):
    """
    数组里的数仅能用一次，和为target的不重复组合数
    :param candidates:
    :param target:
    :return:
    """
    def dfs(candidates, begin, path, res, target):
        if target == 0:
            res.append(path)
            return

        for index in range(begin, size):
            if candidates[index] > target:
                continue
            if index > begin and candidates[index - 1] == candidates[index]:
                continue
            dfs(candidates, index+1, path + [candidates[index]], res, target - candidates[index])

    size = len(candidates)
    if size == 0:
        return []
    path = []
    res = []
    candidates.sort()
    dfs(candidates, 0, path, res, target)
    return res

def combinationSum3(target, k):
    """
    找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
    :param candidates:
    :param target:
    :return:
    """
    def dfs(candidates, begin, size, path, res, target):
        if target == 0 and len(path)==k:
            res.append(path)
            return

        for index in range(begin, size):
            if candidates[index] > target:
                continue
            dfs(candidates, index+1, size, path + [candidates[index]], res, target - candidates[index])

    candidates = [i for i in range(1, 9 + 1)]
    size = len(candidates)

    path = []
    res = []
    candidates.sort()
    dfs(candidates, 0, size, path, res, target)
    return res

print(combine(3, 2))
# print(combinationSum([2,3,6,7],7))
# print(combinationSum2([10,1,2,7,6,1,5],8))
# print(combinationSum3(9,3))


def subsets( nums):
    result = list()
    n = len(nums)

    def backtrace(index, tmp):
        result.append(tmp[:])
        print(result)
        for j in range(index, n):
            backtrace(j + 1, tmp + [nums[j]])

    backtrace(0, [])
    return result

subsets([1,2,3])
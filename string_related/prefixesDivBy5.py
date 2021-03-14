"""
给定由若干 0 和 1 组成的数组 A。我们定义 N_i：从 A[0] 到 A[i] 的第 i 个子数组被解释为一个二进制数（从最高有效位到最低有效位）。

返回布尔值列表 answer，只有当 N_i 可以被 5 整除时，答案 answer[i] 为 true，否则为 false。

"""

def prefixesDivBy5(A):
    # 初始为0，0*2+num[0]开始
    tsum=0
    for i,num in enumerate(A):
        tsum=(tsum*2+num)
        A[i]=(tsum%5==0)
    return A

if __name__ == "__main__":
    a = [0,1,1,1,1,1]

    print(prefixesDivBy5(a))
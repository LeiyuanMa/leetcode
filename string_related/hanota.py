def hanota(A, B, C):
    n = len(A)
    move(n, A, B, C)
# 定义move 函数移动汉诺塔
def move(n, A, B, C):
    if n == 1:
        C.append(A[-1])
        A.pop()
        return
    else:
        move(n-1, A, C, B)  # 将A上面n-1个通过C移到B
        C.append(A[-1])          # 将A最后一个移到C
        A.pop()                  # 这时，A空了
        move(n-1,B, A, C)   # 将B上面n-1个通过空的A移到C



if __name__ == "__main__":
    A = [2, 1, 0]
    B = []
    C = []
    print(hanota(A,B,C))
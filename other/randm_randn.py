"""
首先实现rand5到rand7
然后实现randn到randm
"""
from random import randint
def rand5():
    return randint(1,5)

def rand25():
    return 5*(rand5() -1)+rand5()

def rand7():
    x = float('inf')
    while (x>21):
        x = rand25()

    return x % 7+1

def randn(n):
    return randint(1,5)
def randn2(n):
    return n*(randn(n)-1)+randn(n)

def randm(m,n):
    x = float('inf')
    while(x>m*(n*n/m)):
        x = randn2(n)

    return x%m + 1


if __name__ == "__main__":
    # print(rand7())
    print(randm(7,5))
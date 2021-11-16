def mySqrt(x):
    l, r, ans = 0, x, -1
    while l <= r:
        mid = (l + r) // 2
        if mid * mid <= x:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    if ans*ans == x:
        return True
    else:
        return False
    # return ans


def myPow(x,n):
    if n==0:
        return 1
    if n==1:
        return x
    if n%2==0:
        return myPow(x*x,n//2)
    else:
        return myPow(x*x,n//2)*x


if __name__ == "__main__":
    #print(mySqrt(16))
    print(myPow(2,5))
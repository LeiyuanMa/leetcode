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



if __name__ == "__main__":
    print(mySqrt(16))
"""
给你两个字符串 a 和 b ，它们长度相同。请你选择一个下标，将两个字符串都在 相同的下标 分割开。
由 a 可以得到两个字符串： aprefix 和 asuffix ，满足 a = aprefix + asuffix ，同理，由 b 可以得到两个字符串 bprefix 和 bsuffix ，
满足 b = bprefix + bsuffix 。请你判断 aprefix + bsuffix 或者 bprefix + asuffix 能否构成回文串

"""
def checkPalindromeFormation(a,b):
    # 最简单的两种先判断
    if a[::-1] == a or b == b[::-1]:
        return True
    if a[0] != b[-1] and a[-1] != b[0]:
        return False
    # 双指针
    i, j = 0, len(a)-1
    while i<j:
        if a[i] == b[j]:
            i += 1
            j -= 1
        else: break
    # 中间一段若存在得是回文串
    if i>=j or b[i:j+1] == b[i:j+1][::-1] or a[i:j+1] == a[i:j+1][::-1]:
        return True
    # 换一下再做一遍
    i, j = 0, len(a)-1
    while i<j:
        if b[i] == a[j]:
            i += 1
            j -= 1
        else: break
    if i>=j or a[i:j+1] == a[i:j+1][::-1] or b[i:j+1] == b[i:j+1][::-1] :
        return True
    return False


if __name__ == "__main__":
    a = "uladeedcfd"
    b = "jizeddealu"
    checkPalindromeFormation(a, b)
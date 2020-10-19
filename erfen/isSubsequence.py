def isSubsequence(s, t):
    if not s:
        return True
    if s and not t:
        return False
    p,q=0,0
    while p<len(s) and q<len(t):
        if s[p]==t[q]:
            p+=1
            q+=1
            continue
        else:
            q+=1
    return p==len(s)

if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    isSubsequence(s,t)
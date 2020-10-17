def compressString( S: str) -> str:
    N = len(S)
    res = ''
    i = 0
    while i < N:
        j = i
        while j < N and S[j] == S[i]:
            j += 1
        res += S[i] + str(j - i)
        i = j

    if len(res) < len(S):
        return res
    else:
        return S
print(compressString("aacccccaa"))
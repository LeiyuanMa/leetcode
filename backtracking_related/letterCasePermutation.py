def letterCasePermutation(S):
    def recall(S, start):
        res.append(''.join(S))
        for i in range(start, len(S)):
            # 大写英文
            if 65 <= ord(S[i]) <= 90:
                S[i] = chr(ord(S[i]) + 32)
                recall(S, i + 1)
                S[i] = chr(ord(S[i]) - 32)
            # 小写英文
            elif 97 <= ord(S[i]) <= 122:
                S[i] = chr(ord(S[i]) - 32)
                recall(S, i + 1)
                S[i] = chr(ord(S[i]) + 32)

    res = []
    S = list(S)
    recall(S, 0)
    return res

if __name__ == "__main__":
    S = "a1b2"
    print(letterCasePermutation(S))

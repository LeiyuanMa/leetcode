def reverseOnlyLetters(S):
    letters = [c for c in S if c.isalpha()]
    ans = []
    for c in S:
        if c.isalpha():
            ans.append(letters.pop())
        else:
            ans.append(c)
    return "".join(ans)

if __name__ == "__main__":
    print(reverseOnlyLetters("a-bC-dEf-ghIj"))
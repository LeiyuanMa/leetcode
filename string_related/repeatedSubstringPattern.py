def repeatedSubstringPattern(s):
    return (s + s).find(s, 1) != len(s)

if __name__ == "__main__":
    print(repeatedSubstringPattern("abab"))
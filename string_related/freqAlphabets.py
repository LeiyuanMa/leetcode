def freqAlphabets(s):
    def get(st):
        return chr(int(st) + 96)

    i, ans = 0, ""
    while i < len(s):
        if i + 2 < len(s) and s[i + 2] == '#':
            ans += get(s[i : i + 2])
            i += 2
        else:
            ans += get(s[i])
        i += 1
    return ans

if __name__ == "__main__":
    s = "10#11#12"
    print(freqAlphabets(s))
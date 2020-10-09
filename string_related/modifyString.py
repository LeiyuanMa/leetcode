import string
def modifyString(s):
    alphabet = string.ascii_lowercase
    # 避免可能的边界问题
    s = list(f'0{s}0')
    for i in range(1, len(s)):
        if s[i] == '?':
            for char in alphabet:
                if char != s[i - 1] and char != s[i + 1]:
                    s[i] = char
                    break
    return ''.join(s[1:-1])

if __name__ == "__main__":
    print(modifyString("zs?"))
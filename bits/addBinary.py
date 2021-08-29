"""
模拟加法，实现二进制求和（多进制,divmod参数改为对应进制即可）
"""
def addBinary(a, b):
    if not a or not b:
        return a or b

    a, b, ans = a[::-1], b[::-1], []
    # carry: 进位
    i = j = carry = 0
    while i < len(a) or j < len(b) or carry:
        n1 = int(a[i]) if i < len(a) else 0
        n2 = int(b[j]) if j < len(b) else 0
        carry, cur = divmod(n1 + n2 + carry, 2)
        ans.append(str(cur))
        i, j = i + 1, j + 1
    return ''.join(ans[::-1])

def addTwoNumbers(l1_list, l2_list):
    if l1_list[0] == 0:
        return l2_list
    if l2_list[0] == 0:
        return l1_list
    l1_list.reverse()
    l2_list.reverse()
    result = list()
    carry = 0
    while l1_list or l2_list or carry:
        n1 = l1_list.pop() if l1_list else 0
        n2 = l2_list.pop() if l2_list else 0
        carry, ans = divmod(n1 + n2 + carry, 10)
        result.append(ans)

    return result

if __name__ == "__main__":
    # a = "11"
    # b = "1"
    # print(addBinary(a,b))
    a = [0,8,6,5,6,8,3,5,7]
    b = [6,7,8,0,8,5,8,9,7]
    print(addTwoNumbers(a,b))
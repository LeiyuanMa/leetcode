# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: numDecodings.py
@time: 2021/10/28 21:38
@desc: 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：

'A' -> 1
'B' -> 2
...
'Z' -> 26
要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：

"AAJF" ，将消息分组为 (1 1 10 6)
"KJF" ，将消息分组为 (11 10 6)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-ways
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def numDecodings(s: str) -> int:
    n = len(s)
    s = ' ' + s
    f = [0] * (n + 1)
    f[0] = 1
    for i in range(1, n + 1):
        a = ord(s[i]) - ord('0')
        b = (ord(s[i - 1]) - ord('0')) * 10 + ord(s[i]) - ord('0')
        if 1 <= a <= 9:
            f[i] = f[i - 1]
        if 10 <= b <= 26:
            f[i] += f[i - 2]
    return f[n]


s = "06"
print(numDecodings(s))
# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: KMP.py
@time: 2021/8/17 16:35
@desc: 哈哈哈，根据自己理解写的，果然超时了
'''

# def get_prefix_table(pattern_str):
#     prefix_table = [-1, 0]
#     length = len(pattern_str)
#     for i in range(2,length):
#         current_str = pattern_str[:i]
#         current_str_len = len(current_str)
#         cnt = 0
#         for i in range(1, current_str_len):
#             if current_str[:i] == current_str[(current_str_len-i):]:
#                 cnt = i
#         prefix_table.append(cnt)
#     return prefix_table

def get_prefix_table(pattern_str):
    a = len(pattern_str)
    next = ['' for i in range(a)]
    j, k = 0, -1
    next[0] = k
    while (j < a - 1):
        if k == -1 or pattern_str[k] == pattern_str[j]:
            k += 1
            j += 1
            next[j] = k
        else:
            k = next[k]
    return next


def find_str(p, pattern_str, prefix_table):
    i,j = 0,0
    while i < len(p) and j < len(pattern_str):
        if j == -1:
            i += 1
            j = 0
        elif p[i] == pattern_str[j]:
            i += 1
            j += 1
            print(i,j)
        else:
            j = prefix_table[j]
    if j == len(pattern_str):
        return i-j
    else:
        return -1
pattern_str = "ababc"
p = "aaaaa"
prefix_table = get_prefix_table(pattern_str)
print(prefix_table)
print(find_str(p, pattern_str, prefix_table))
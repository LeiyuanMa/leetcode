# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: flatten_arr.py
@time: 2021/11/13 14:49
@desc: 
'''

def flatten(input_arr, output_arr=None):
    if output_arr is None:
        output_arr = []
    for ele in input_arr:
        if isinstance(ele, list): # 判断ele是否可迭代
            flatten(ele, output_arr) # 尾数递归
        else:
            output_arr.append(ele) # 产生结果
    return output_arr

t = [1, [2, [ [3, 4], 5, []], 6]]
print(flatten(t))
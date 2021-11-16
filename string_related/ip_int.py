# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: ip_int.py
@time: 2021/10/17 18:00
@desc: 
'''

# int-->ip
ch2 = lambda x: '.'.join([str(x // (256 ** i) % 256) for i in range(3, -1, -1)])
ch2(123456789)
# ip-->int
ch3 = lambda x:sum([256**j*int(i) for j,i in enumerate(x.split('.')[::-1])])
ch3('7.91.205.21')
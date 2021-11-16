# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: corpFlightBookings.py
@time: 2021/8/31 21:11
@desc: 
'''


def corpFlightBookings(bookings, n):
    result = dict()
    res = list()
    for booking in bookings:
        num = booking[-1]
        for i in range(booking[0], booking[1] + 1):
            if i in result:
                result[i] += num
            else:
                result[i] = num
    for k, v in result.items():
        res.append((k, v))
    res.sort(key=lambda x: x[0])
    return [t[1] for t in res]

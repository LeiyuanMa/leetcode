# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: maxPoints.py
@time: 2021/11/16 22:45
@desc: 
'''
from decimal import Decimal


def maxPoints(points):
    num_point = len(points)
    if num_point <= 0:
        return 0
    if num_point == 1:
        return 1
    if num_point == 2:
        return 2
    result = 0
    for index1 in range(num_point):
        myHashMap = {'inf': 0}
        twinsPoint = 0
        for index2 in range(index1+1, num_point):
            if points[index1][0] == points[index2][0] and points[index1][1] != points[index2][1]:
                myHashMap['inf'] += 1
            elif points[index1][0] != points[index2][0]:
                slope = mySlope(points[index1], points[index2])
                if slope in myHashMap:
                    myHashMap[slope] += 1
                else:
                    myHashMap[slope] = 1
            else:
                twinsPoint += 1
        result = max(result, max(myHashMap.values()) + twinsPoint)
    return result + 1


def mySlope(num1, num2):
    return Decimal(num2[1] - num1[1]) / Decimal(num2[0] - num1[0])


points = [[1,1],[2,2],[3,3]]
print(maxPoints(points))

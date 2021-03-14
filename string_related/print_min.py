# -*- coding:utf-8 -*-
from functools import cmp_to_key
class Solution:
    def compare(self, num1, num2):
        t = str(num1) + str(num2)
        s = str(num2) + str(num1)
        if t > s:
            return 1
        elif t < s:
            return -1
        else:
            return 0

    def PrintMinNumber(self, numbers):
        # write code here
        if numbers is None:
            return ""
        lens = len(numbers)
        if lens == 0:
            return ""
        tmpNumbers = sorted(numbers, key=cmp_to_key(self.compare))
        return int(''.join(str(x) for x in tmpNumbers))


print(Solution().PrintMinNumber([3, 32, 321]))


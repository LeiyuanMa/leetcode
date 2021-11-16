# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: removeNthFromEnd.py
@time: 2021/9/9 16:33
@desc: 
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n: int) :
    dummy = ListNode(0)
    dummy.next = head
    fast, slow = head, dummy
    for _ in range(n):
        fast = fast.next
    while fast and slow:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next
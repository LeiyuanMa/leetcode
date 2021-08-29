# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: mergeTwoLists.py
@time: 2021/8/27 11:23
@desc: 
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
head = ListNode(1)
t2 = ListNode(2)
t3 = ListNode(3)
t4 = ListNode(4)
t5 = ListNode(5)
t2.next = t4
head.next = t2

l2 = ListNode(1)
l2.next = t3
t3.next = t4
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    result = ListNode(0)
    pre = result
    while l1 and l2:
        if l1.val > l2.val:
            pre.next = l2
            l2 = l2.next
        else:
            pre.next = l1
            l1 = l1.next
        pre = pre.next
    pre.next = l1 if l1 is not None else l2

    return result.next


mergeTwoLists(head, l2)
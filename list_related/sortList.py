# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: sortList.py
@time: 2021/8/30 21:37
@desc: 归并排序，排序列表
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head: ListNode, tail: ListNode) -> ListNode:
    if not head:
        return head
    if head.next == tail:
        head.next = None
        return head
    slow = fast = head
    while fast != tail:
        slow = slow.next
        fast = fast.next
        if fast != tail:
            fast = fast.next
    return merge(sortList(head, slow), sortList(slow, tail))


def merge(head, head2):
    dummy = ListNode(-1)
    tmp = dummy
    while head and head2:
        if head.val <= head2.val:
            tmp.next = head
            head = head.next
        else:
            tmp.next = head2
            head2 = head2.next
        tmp = tmp.next
    if head:
        tmp.next = head
    if head2:
        tmp.next = head2
    return dummy.next


head = ListNode(4)
t1 = ListNode(2)
t2 = ListNode(1)
t3 = ListNode(3)
head.next = t1
t1.next = t2
t2.next = t3
result = sortList(head, None)
t=1


"""
双指针删除倒数第k个节点
1-2-3-4-5
k:2
k:        0->1
former:1->2->3->4->5->null
latter:      1->2->3->4
"""
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None
head = Node(1)
t2 = Node(2)
t3 = Node(3)
t4 = Node(4)
t5 = Node(5)
t4.next = t5
t3.next = t4
t2.next = t3
head.next = t2

def getKthFromEnd(head, k):
    fast, slow = head, head

    while fast and k > 0:
        fast, k = fast.next, k - 1
    while fast:
        fast, slow = fast.next, slow.next

    return slow


result = getKthFromEnd(head, 2)
t=1
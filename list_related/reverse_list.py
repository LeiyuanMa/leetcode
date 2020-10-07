"""
参考博客：https://www.cnblogs.com/mwl523/p/10749144.html
就地翻转
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head):
    if head == None:
        return head
    dummy = ListNode(-1)
    dummy.next = head
    prev = dummy.next
    pCur = prev.next
    while (pCur != None):
        prev.next = pCur.next
        pCur.next = dummy.next
        dummy.next = pCur
        pCur = prev.next
    return dummy.next


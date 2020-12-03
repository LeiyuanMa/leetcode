"""
参考博客：https://www.cnblogs.com/mwl523/p/10749144.html
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head):
    """原地翻转"""
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

def reverseList2(head):
    """新建链表翻转"""
    dummy = ListNode(-1)
    pCur = head
    while(pCur!= None):
        pNext = pCur.next
        pCur.next = dummy.next
        dummy.next = pCur
        pCur = pNext
    return dummy.next

if __name__ == "__main__":
    head = ListNode(1)
    next_2 = ListNode(2)
    next_3 = ListNode(3)
    next_4 = ListNode(4)
    next_5 = ListNode(5)
    head.next = next_2
    next_2.next = next_3
    next_3.next = next_4
    next_4.next = next_5
    reversed_list = reverseList2(head)

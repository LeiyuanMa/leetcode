"""
检查输入的链表是否是回文的。

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if not head: return True
    slow = head
    fast = head

    # slow 遍历到中间，最后 slow 停的位置是 n/2+1
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 然后从 slow 开始反转链表
    # 如果是奇数，多出来的一个节点不用管了
    pre = slow
    while slow and slow.next:
        tmp = slow.next.next
        slow.next.next = pre
        pre = slow.next
        slow.next = tmp

    # 反转后的头结点是 pre，从 pre 和 head 开始比较 val
    while head and pre:
        if head.val != pre.val:
            return False
        head = head.next
        pre = pre.next

    return True


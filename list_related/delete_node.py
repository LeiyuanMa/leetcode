"""
给定链表和要删除的节点值，完成节点的删除
"""
def deleteNode(head,val):
    if head.val == val:
        return head.next
    pre, cur = head, head.next
    while cur and cur.val != val:
        pre, cur = cur, cur.next
    # 若 cur 指向 nullnull ，代表链表中不包含值为 val 的节点
    if cur:
        pre.next = cur.next
    return head
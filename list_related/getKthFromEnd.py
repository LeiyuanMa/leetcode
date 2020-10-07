"""
双指针删除倒数第k个节点
1-2-3-4-5
k:2
k:        0->1
former:1->2->3->4->5->null
latter:      1->2->3->4
"""
def getKthFromEnd(head, k):
    former, latter = head, head
    for _ in range(k):
        former = former.next
    while former:
        former, latter = former.next, latter.next
    return latter
"""
寻找两个链表的第一个公共节点
"""
def getIntersectionNode(headA, headB):
    node1, node2 = headA, headB

    while node1 != node2:
        # 这里注意交换列表！！！
        node1 = node1.next if node1 else headB
        node2 = node2.next if node2 else headA

    return node1
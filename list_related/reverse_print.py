"""
利用辅助栈
时间复杂度 O(N)： 入栈和出栈共使用 O(N)时间。
空间复杂度 O(N)： 辅助栈 stack 和数组 res 共使用 O(N)的额外空间。
"""
def reversePrint(head):
    stack = []
    while head:
        stack.append(head.val)
        head = head.next
    return stack[::-1]
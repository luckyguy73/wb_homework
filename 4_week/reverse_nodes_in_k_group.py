# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head:
            node = head
            for _ in range(k - 1):
                node = node.next
                if not node:
                    return head
            prev = self.reverseKGroup(node.next, k)
            while prev is not node:
                prev, head.next, head = head, prev, head.next
            return prev

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        c1, c2 = dummy, dummy
        for _ in range(m - 1):
            c1 = c1.next
        for _ in range(n + 1):
            c2 = c2.next
        h = c2
        a = c1.next
        b = a.next
        while True:
            a.next = h
            if b == c2:
                break
            h = a
            a = b
            b = b.next
        c1.next = a
        return dummy.next

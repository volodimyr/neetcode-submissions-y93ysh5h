# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        from math import gcd
        while cur.next:
            tmp = cur.next
            g = gcd(cur.val, tmp.val)
            node = ListNode(g, cur.next)
            cur.next = node
            cur = tmp
        return head
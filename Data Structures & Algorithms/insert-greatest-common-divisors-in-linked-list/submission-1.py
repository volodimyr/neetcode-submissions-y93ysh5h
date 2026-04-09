class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a
        while cur.next:
            tmp = cur.next
            g = gcd(cur.val, tmp.val)
            node = ListNode(g, cur.next)
            cur.next = node
            cur = tmp
        return head
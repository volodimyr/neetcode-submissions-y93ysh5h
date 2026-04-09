class Solution:
    def isPalindrome(self, head: Optional[ListNode])->bool:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        
        cur = head
        while prev:
            if prev.val != cur.val:
                return False
            prev= prev.next
            cur = cur.next
        
        return True
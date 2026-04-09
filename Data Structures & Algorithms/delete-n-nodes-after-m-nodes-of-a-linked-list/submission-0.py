# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        
        cur = head
        while cur:
            i = 0
            while cur and i < m-1:
                cur = cur.next
                i += 1
            if not cur:
                break
            
            prev = cur
            j = 0
            while cur and j <= n:
                cur = cur.next 
                j += 1
            prev.next = cur
        return head
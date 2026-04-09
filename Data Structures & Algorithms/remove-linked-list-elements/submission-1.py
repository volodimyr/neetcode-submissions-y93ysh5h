# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        cur = head
        prev = dummy
        while cur:
            if cur.val != val:
                prev.next = cur
                prev = prev.next
            else:
                prev.next = None
            cur = cur.next

        
        return dummy.next
        
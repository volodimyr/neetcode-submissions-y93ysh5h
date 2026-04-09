# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        
        L, R = 0, len(arr)-1
        while L < R:
            if arr[L] != arr[R]:
                return False
            L+=1
            R-=1
        
        return True
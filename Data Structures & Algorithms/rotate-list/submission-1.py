# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        
        def rotate(L, R):
            while L < R:
                arr[L], arr[R] = arr[R], arr[L]
                L += 1
                R -= 1

        if k > len(arr):
            k = k % len(arr)
        rotate(0, len(arr)-1)
        rotate(0, k-1)
        rotate(k, len(arr)-1)

        cur = head
        i = 0
        while cur:
            cur.val = arr[i]
            i+=1
            cur = cur.next

        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        if len(lists) == 1:
            return lists[0]
        
        M = len(lists)//2
        left = self.mergeKLists(lists[M:])
        right = self.mergeKLists(lists[:M])
        return self.merge(left, right)
    
    def merge(self, l1, l2):
        res = ListNode()
        curr = res
        curl1, curl2 = l1, l2
        while curl1 and curl2:
            if curl1.val < curl2.val:
                curr.next = curl1
                curl1 = curl1.next
            else:
                curr.next = curl2
                curl2 = curl2.next
            curr = curr.next
        if curl1:
            curr.next = curl1
        if curl2:
            curr.next = curl2
        
        return res.next
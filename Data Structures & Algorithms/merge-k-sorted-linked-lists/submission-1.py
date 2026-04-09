# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Node:
    def __init__(self, n):
        self.n = n
    
    def __lt__(self, other):
        return self.n.val < other.n.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        for l in lists:
            heapq.heappush(h, Node(l))
        
        res = ListNode()
        cur = res
        while h:
            node = heapq.heappop(h)
            cur.next = ListNode(node.n.val)
            cur = cur.next
            if node.n.next:
                heapq.heappush(h, Node(node.n.next))
        
        return res.next

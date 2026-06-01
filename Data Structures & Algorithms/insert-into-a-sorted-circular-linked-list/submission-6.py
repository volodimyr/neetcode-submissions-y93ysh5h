# Definition for a Node.
# class Node:
#   def __init__(self, val=None, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            nNode = Node(insertVal)
            nNode.next = nNode
            return nNode
        
        biggest = head

        real_head = head
        cur = head
        while True:
            if biggest.val < cur.val:
                biggest = cur
            if real_head.val >= cur.val:
                real_head = cur
            cur = cur.next
            if cur == head:
                break
        
        real_tail = None
        cur = head
        while True:
            if cur.next == real_head:
                real_tail = cur
                break
            cur = cur.next

        if biggest.val > real_tail.val:
            real_tail = biggest
            real_head = biggest.next

        nNode = Node(insertVal)
        if insertVal < real_head.val or insertVal > real_tail.val:
            real_tail.next, nNode.next= nNode, real_tail.next
        else:
            cur = head
            while True:
                if cur.val <= insertVal <= cur.next.val:
                    cur.next, nNode.next = nNode, cur.next
                    break
                
                cur = cur.next

        
        return head
        
        


        
        
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        q = deque()
        q.append(root)
        while q:
            prev = None
            for i in range(len(q)):
                pop = q.popleft()
                if pop.left:
                    q.append(pop.left)
                if pop.right:
                    q.append(pop.right)
                if prev:
                    prev.next = pop
                prev = pop
        return root
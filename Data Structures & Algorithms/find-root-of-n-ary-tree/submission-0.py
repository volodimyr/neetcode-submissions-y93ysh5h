"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        childs = set()


        def dfs(root):
            if not root:
                return
            
            for ch in root.children:
                if ch.val not in childs:
                    childs.add(ch.val)
                    dfs(ch)
                

        for t in tree:
            dfs(t)
        
        for t in tree:
            if t.val not in childs:
                return t
        
        return None
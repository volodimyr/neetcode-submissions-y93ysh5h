"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        m = {}
        def dfs(root):
            if root.val in m:
                return m[root.val]
            coppy = Node(root.val)
            m[root.val] = coppy
            for n in root.neighbors:
                coppy.neighbors.append(dfs(n))

            return coppy
        return dfs(node)
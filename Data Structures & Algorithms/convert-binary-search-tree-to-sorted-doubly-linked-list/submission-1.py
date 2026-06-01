"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        arr = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            arr.append(root)
            inorder(root.right)

        inorder(root)


        for i in range(len(arr)):
            arr[i].right = arr[i+1] if i + 1 < len(arr) else None
            arr[i].left = arr[i-1] if i - 1 >= 0 else None
        
        arr[0].left = arr[len(arr)-1]
        arr[len(arr)-1].right = arr[0]
        
        return arr[0]
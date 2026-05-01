# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        completed = [False]
        def complete(arr):
            for a in arr:
                if completed[0] and a:
                    return False
                if not a:
                    completed[0] = True
            return True
            
        arr = []
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                arr.append(node)
                if node:
                    q.append(node.left)
                    q.append(node.right)

        
        return complete(arr)
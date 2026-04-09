# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        paths = []
        def dfs(root, path):
            if not root:
                return
            
            path.append(str(root.val))
            if not root.left and not root.right:
                paths.append(path[:])
            dfs(root.left, path)
            dfs(root.right, path)
            path.pop()
        
        dfs(root, [])

        res = 0
        for row in paths:
            res += int(''.join(row))
        
        return res
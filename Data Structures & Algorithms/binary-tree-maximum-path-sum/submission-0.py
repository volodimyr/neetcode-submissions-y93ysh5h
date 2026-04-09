# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -math.inf
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            local = max(root.val, left+root.val, right+root.val)

            res = max(res, local, root.val+left+right, root.val+left, root.val + right)
            return local

        dfs(root)
        return res
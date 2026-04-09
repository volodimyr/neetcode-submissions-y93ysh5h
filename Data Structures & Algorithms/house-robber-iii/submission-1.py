# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def dfs(root, taken):
            if not root:
                return 0
            res = 0
            if root.left and not taken:
                res += max(dfs(root.left, False), root.left.val+dfs(root.left, True))
            elif root.left:
                res += dfs(root.left, False)
            if root.right and not taken:
                res += max(dfs(root.right, False), root.right.val+dfs(root.right, True))
            elif root.right:
                res += dfs(root.right, False)
            return res
        
        return max(dfs(root, False), root.val+dfs(root, True))

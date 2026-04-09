# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(root, parent, cons):
            res[0] = max(res[0], cons)
            if not root:
                return
            if parent and root.val - parent.val == 1:
                cons += 1
            else:
                cons = 1
            dfs(root.left, root, cons)
            dfs(root.right, root, cons)
        
        dfs(root, None, 1)

        return res[0]
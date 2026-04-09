# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = [math.inf]
        def dfs(root):
            if not root:
                return 
            if abs(root.val - target) < abs(res[0]-target):
                res[0] = root.val
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return res[0]
            